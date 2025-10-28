from modules.post.infra.factory.controller_factory import ControllerFactory
from infra.adapter_factory import AdapterFactory

from PyQt5.QtWidgets import QApplication, QMainWindow

from dotenv import load_dotenv
load_dotenv()


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        adapter_factory = AdapterFactory()
        self.post_controller_factory = ControllerFactory(adapter_factory)

        self.post_controller = self.post_controller_factory.generate_post_ui_controller()
        self.setCentralWidget(self.post_controller.ui)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
