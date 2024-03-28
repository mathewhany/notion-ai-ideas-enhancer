from abc import ABC, abstractmethod


class IdeaEnhancer(ABC):
    @abstractmethod
    def process(self, idea: str) -> dict[str, str]:
        pass
