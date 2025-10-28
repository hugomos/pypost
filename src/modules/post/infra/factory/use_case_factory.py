from infra.adapter_factory import AdapterFactory

from modules.post.application.use_case.generate_post import GeneratePost


class UseCaseFactory:
    def __init__(self, adapter_factory: AdapterFactory):
        self.adapter_factory = adapter_factory

    def generate_post(self):
        return GeneratePost(self.adapter_factory.ai_agent())
