from abc import ABC
from .. import Idea

class BaseIdeaManagerAdapter(ABC):
    def add_idea(self, idea: Idea):
        pass
