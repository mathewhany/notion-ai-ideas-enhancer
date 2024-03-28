from .idea_manager_adapter import BaseIdeaManagerAdapter
from .idea_enhancers import IdeaEnhancer
from . import Idea


class IdeaProcessor:
    def __init__(
        self, ideas_manager: BaseIdeaManagerAdapter, enhancers: list[IdeaEnhancer] = []
    ) -> None:
        self._enhancers = enhancers
        self._ideas_manager = ideas_manager

    def create_idea_from_text(self, idea_text: str) -> Idea:
        extras = {}

        for enhancer in self._enhancers:
            extras.update(enhancer.process(idea_text))

        return Idea(idea_text, extras)

    def process(self, idea_text: str):
        idea = self.create_idea_from_text(idea_text)
        self._ideas_manager.add_idea(idea)
        return idea
