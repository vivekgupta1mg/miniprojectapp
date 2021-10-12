import ujson as json
from torpedo import CONFIG
from torpedo.task import Task, TaskExecutor
from ...models import Answers
from ..app import Base as DB
from ...managers.user import UserManager
from ...managers.question import QuestionManager


class AnswerManager:
    config = CONFIG.config

    @classmethod
    async def get_answers(cls, request):
        answers = await Answers.all()
        return answers

    @classmethod
    async def get_answer_by_id(cls, request,id):
        answers = await Answers.get(id=id)
        return answers

    @classmethod
    async def create_answer(cls,payload):

        # user_id = await UserManager.get_user_by_id({"username": "vivek"})
        # question_id = await QuestionManager.get_question_by_id({"id": 22})

        # payload = {"question_id": question_id, "user_id": user_id, "answer_text": "python is simple?",
        #            "votes": 1, "accepted": True}
        payload = await DB.create_instance(Answers, payload)
        return payload
