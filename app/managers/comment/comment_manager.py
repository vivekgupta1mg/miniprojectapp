import ujson as json
from torpedo import CONFIG
from torpedo.task import Task, TaskExecutor

from app.managers.answer.answer_manager import AnswerManager
from ...models import Comments
from ..app import Base as DB
from ...managers.user import UserManager
from ...managers.question import QuestionManager
from ...managers.answer import AnswerManager


class CommentManager:
    config = CONFIG.config

    @classmethod
    async def get_comments(cls, request):
        comments = await Comments.all()
        return comments

    @classmethod
    async def get_comment_by_id(cls, request, id):
        comments = await Comments.get(id=id)
        return comments

    @classmethod
    async def create_comment(cls, payload):
        # user_id = await UserManager.get_user_by_id({"username": "vivek"})
        # question_id = await QuestionManager.get_question_by_id({"id": 22})
        # answer_id = await AnswerManager.get_answer_by_id({"id": 1})
        # question_entity_id = await QuestionManager.get_question_by_id({"id": 22})
        # answer_entity_id = await AnswerManager.get_answer_by_id({"id": 1})

        # payload = {"question_id": question_id, "user_id": user_id, "answer_id": answer_id, "question_entity_id":
        #            question_entity_id, "answer_entity_id": answer_entity_id, "entity_type": 1, "comment_text": "good"}
        payload= await DB.create_instance(Comments, payload)
        return payload
