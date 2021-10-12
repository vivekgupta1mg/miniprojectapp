import ujson as json
from torpedo import CONFIG
from torpedo.task import Task, TaskExecutor
from ...models import Questions
from ..app import Base as DB
from ...managers.user import UserManager


class QuestionManager:
    config = CONFIG.config

    @classmethod
    async def get_questions(cls, request):
        questions = await Questions.all()
        return questions

    @classmethod
    async def get_question_by_id(cls, payload):
        questions = await Questions.get(id=payload["id"])
        
        return questions

    @classmethod
    async def create_question(cls, request):
        user_id = await UserManager.get_user_by_id({"username": "vivek"})

        payload = {"user_id": user_id, "question_text": "how is python?",
                   "description": "nothing have to describe!", "answered": True}
        questions = await DB.create_instance(Questions, payload)
        return questions
