import os
import google.generativeai as genai
from .ai_adapter import GeminiAdapter

from .idea_processor import IdeaProcessor
from .idea_manager_adapter import NotionIdeaManagerAdapter
from .idea_enhancers import AITitleGenerator, AIIconGenerator
from .idea_manager_adapter.notion_middlewares import (
    AITitleGeneratorNotionMiddleware,
    AIIconGeneratorNotionMiddleware,
)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NOTION_API_KEY = os.getenv("NOTION_API_KEY")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

genai.configure(api_key=GEMINI_API_KEY)

gen_ai_model = GeminiAdapter(model=genai.GenerativeModel("gemini-pro"))

idea_manager = NotionIdeaManagerAdapter(
    api_key=NOTION_API_KEY,
    database_id=NOTION_DATABASE_ID,
    request_middlewares=[
        AITitleGeneratorNotionMiddleware(),
        AIIconGeneratorNotionMiddleware(),
    ],
)

idea_processor = IdeaProcessor(
    ideas_manager=idea_manager,
    enhancers=[AITitleGenerator(gen_ai_model), AIIconGenerator(gen_ai_model)],
)
