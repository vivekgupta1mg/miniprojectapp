from sanic import Sanic, Blueprint
from .question_details import question_details
from .answer_details import answer_details
from .comment_details import comment_details
from .rating_details import rating_details
from .user_details import user_details
from .so_basictest import so_basictest


# from  sanic_openapi import openapi2_blueprint


blueprint_group = Blueprint.group(
    user_details, question_details, answer_details, comment_details, rating_details, so_basictest,
)
