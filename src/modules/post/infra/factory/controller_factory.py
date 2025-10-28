from .use_case_factory import UseCaseFactory
from ...generate_post_ui_controller import GeneratePostUIController
from ...ui.generate_post_widget import GeneratePostWidget
from infra.adapter_factory import AdapterFactory


class ControllerFactory:
    def __init__(self, adapter_factory: AdapterFactory):
        self.use_case_factory = UseCaseFactory(adapter_factory)

    def generate_post_ui_controller(self):
        return GeneratePostUIController(
            ui=GeneratePostWidget(),
            generate_markdown_post_use_case=self.use_case_factory.generate_markdown_post()
        )
