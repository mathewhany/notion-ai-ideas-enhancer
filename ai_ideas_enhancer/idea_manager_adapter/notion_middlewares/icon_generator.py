from requests import Request
from ai_ideas_enhancer import Idea
from . import NotionRequestMiddleware


class AIIconGeneratorNotionMiddleware(NotionRequestMiddleware):
    def process_request(self, idea: Idea, request: Request):
        request.json.update(
            {
                "icon": {
                    "emoji": idea.extras["icon"]
                }
            }
        )
