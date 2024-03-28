from requests import Request
from ai_ideas_enhancer.idea import Idea
from . import NotionRequestMiddleware


class AITitleGeneratorNotionMiddleware(NotionRequestMiddleware):
    def process_request(self, idea: Idea, request: Request):
        request.json.update(
            {
                "properties": {
                    "Name": {"title": [{"text": {"content": idea.extras["title"]}}]}
                },
            }
        )
