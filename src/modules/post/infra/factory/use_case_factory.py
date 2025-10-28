from infra.adapter_factory import AdapterFactory

from modules.post.application.use_case.generate_markdown_post import GenerateMarkdownPost


class UseCaseFactory:
    def __init__(self, adapter_factory: AdapterFactory):
        self.adapter_factory = adapter_factory

    def generate_markdown_post(self):
        return GenerateMarkdownPost(self.adapter_factory.ai_agent())
