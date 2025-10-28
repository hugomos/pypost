import os
from PyQt5.QtWidgets import QFileDialog

from infra.ui_controller import UI_Controller
from .ui.generate_post_widget import GeneratePostWidget
from .application.use_case.generate_post import GeneratePost

from markdown import markdown
from slug import slug

class GeneratePostUIController(UI_Controller):
    def __init__(
        self,
        ui: GeneratePostWidget,
        generate_post_use_case: GeneratePost
    ):
        UI_Controller.__init__(self)

        self.ui = ui
        self.generate_post_use_case = generate_post_use_case

        self.ui.exec_button.clicked.connect(self.execute)
        self.ui.explorer_button.clicked.connect(self.select_output_dir)

        self._init_ui()

    def _set_is_loading(self, is_loading):
        self.ui.exec_button.setEnabled(not is_loading)
        self.ui.exec_button.setText("Aguarde..." if is_loading else "Executar")
        self.ui.exec_button.repaint()

    def _init_ui(self):
      self.ui.output_dir_line_edit.setText(os.path.abspath(os.path.expanduser("~")))

    def select_output_dir(self):
        output_dir_path = QFileDialog.getExistingDirectory(
          None,
          "Select Output Directory",
          os.path.expanduser("~"),
          QFileDialog.ShowDirsOnly
        )

        if output_dir_path:
            output_dir_path = os.path.abspath(output_dir_path)
            self.ui.output_dir_line_edit.setText(output_dir_path)
            self.ui.output_dir_line_edit.repaint()

        return

    def set_previewer(self, output, output_type):
      if output_type == "markdown":
        html_content = markdown(output, extensions=["fenced_code", "nl2br"])
        self.ui.post_text_edit.setHtml(html_content)
      elif output_type == "html":
        self.ui.post_text_edit.setHtml(output)
      else:
        self.ui.post_text_edit.setPlainText(output)

    def execute(self):
        self._set_is_loading(True)

        subject = self.ui.subject_line_edit.text().strip()
        keywords = self.ui.keywords_line_edit.text().strip()

        if not subject:
            self._set_is_loading(False)
            self.show_box_error("O assunto é obrigatório")
            return

        output_type = self.ui.output_type_combo_box.currentText()

        if output_type == "Select...":
            self._set_is_loading(False)
            self.show_box_error("O formato do arquivo gerado é obrigatório")
            return

        output_type = output_type.replace(" ", "").lower()
        output_extension = {"markdown": "md", "html": "html", "plaintext": "txt"}[output_type]

        output_dir = self.ui.output_dir_line_edit.text().strip()

        if not output_dir:
            self._set_is_loading(False)
            self.show_box_error("A diretorio de destino é obrigatório")
            return

        input_ = {
            "subject": subject,
            "keywords": keywords.replace(", ", ","),
            "output_type": output_type
        }

        response = self.generate_post_use_case.perform(input_)
        if response.is_left():
            self._set_is_loading(False)
            self.show_box_error(str(response.value))
            return

        file_name = slug(subject).replace(" ", "_")
        output_path = os.path.abspath(os.path.join(output_dir, f"{file_name}.{output_extension}"))

        output_content = response.value.replace(f"```{output_type}", "").replace("```", "")

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(output_content)
            file.close()

        self.set_previewer(output_content, output_type)

        self._set_is_loading(False)
        self.show_box_success(
          f"Post: {subject} gerado com sucesso e salvo em {output_path.split(os.path.expanduser('~'))[-1]}"
        )
