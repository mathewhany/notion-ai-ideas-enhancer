from requests import Request, Response
from ... import Idea


from abc import ABC, abstractmethod


class NotionRequestMiddleware(ABC):
    @abstractmethod
    def process_request(self, idea: Idea, request: Request):
        pass


class NotionResponseMiddleware(ABC):
    @abstractmethod
    def process_response(self, idea: Idea, response: Response):
        pass
