from abc import ABC, abstractmethod


class BaseGenAIAdapter(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
