import requests

from .notion_middlewares import NotionRequestMiddleware, NotionResponseMiddleware
from .. import Idea
from . import BaseIdeaManagerAdapter


class NotionIdeaManagerAdapter(BaseIdeaManagerAdapter):
    def __init__(
        self,
        api_key: str,
        database_id: str,
        request_middlewares: list[NotionRequestMiddleware] = [],
        response_middlewares: list[NotionResponseMiddleware] = [],
    ):
        self.database_id = database_id
        self.api_key = api_key
        self.request_middleware = request_middlewares
        self.response_middleware = response_middlewares

    def add_idea(self, idea: Idea):
        req_body = {
            "parent": {"database_id": self.database_id},
            "properties": {"Name": {"title": [{"text": {"content": idea.content}}]}},
            "children": [
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": idea.content,
                                },
                            }
                        ]
                    },
                }
            ],
        }

        req_headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28",
        }

        req = requests.Request(
            "POST",
            "https://api.notion.com/v1/pages",
            json=req_body,
            headers=req_headers,
        )

        for middleware in self.request_middleware:
            middleware.process_request(idea, req)

        session = requests.Session()
        res = session.send(req.prepare())

        if res.status_code != 200:
            raise Exception(f"Failed to add {idea} to Notion")

        for middleware in self.response_middleware:
            middleware.process_response(idea, res)
