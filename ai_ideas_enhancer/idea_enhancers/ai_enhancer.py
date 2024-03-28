from typing import Callable
from ..ai_adapter import BaseGenAIAdapter
from .idea_enhancer import IdeaEnhancer


class AIEnhancer(IdeaEnhancer):
    def __init__(self, model: BaseGenAIAdapter) -> None:
        self.model = model

    def _generate(
        self,
        prompt: str,
        max_tries: int = 3,
        max_length: int = 1000,
        acceptence_criteria: Callable[[str], bool] = lambda _: True,
    ) -> str | None:
        for _ in range(max_tries):
            response = self.model.generate(prompt)
            if response is not None and 0 < len(response) <= max_length and acceptence_criteria(response):
                return response

        raise Exception(f"Failed to generate text for prompt: {prompt}")
