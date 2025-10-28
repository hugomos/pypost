from abc import ABC, abstractmethod


class Agent(ABC):
    @abstractmethod
    def prompt(self, prompt: str, **kwargs) -> str | None:
        pass
