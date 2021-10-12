import ujson as json
from torpedo import CONFIG
from torpedo.task import Task, TaskExecutor

from app.managers.answer.answer_manager import AnswerManager
from ...models import Ratings
from ..app import Base as DB
from ...managers.user import UserManager
from ...managers.question import QuestionManager

class RatingManager:
    config = CONFIG.config

    @classmethod
    async def get_ratings(cls, request):
        ratings = await Ratings.all()
        return ratings

    @classmethod
    async def get_rating_by_id(cls, request, rating_id):
        ratings = await Ratings.get(id=rating_id)
        return ratings

    @classmethod
    async def create_rating(cls, request):
        user_id = await UserManager.get_user_by_id({"username": "vivek"})
        question_id = await QuestionManager.get_question_by_id({"id": 22})
        answer_id = await AnswerManager.get_answer_by_id({"id": 1})

        payload = {"question_id": question_id, "user_id": user_id, "answer_id": answer_id, "rating_star": 4}
        ratings = await DB.create_instance(Ratings, payload)
        return ratings


       