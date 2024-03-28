
from requests import Response
from ai_ideas_enhancer.idea import Idea
from . import NotionResponseMiddleware


class OpenPageNotionMiddleware(NotionResponseMiddleware):
    def process_response(self, idea: Idea, response: Response):
        data = response.json()
        print(data)
