from torpedo import Request, send_response
from sanic import Blueprint, Sanic
from sanic.response import json
from ..managers.question import QuestionManager
from pydantic import ValidationError
from ..decorators.question import question_validate
from ..validation.check_payload import Check
import json

question_details = Blueprint("question_details", url_prefix="/question_details", version=4)



@question_validate()
@question_details.route("/", methods=["GET"])
async def show_question(request):
    _response = await QuestionManager.get_questions(request)
    return send_response({'message': json.dumps(
        _response, indent=4, sort_keys=True, default=str)})


@question_validate()
@question_details.route("/<id:int>", methods=["GET"])
async def show_question_by_id(request, id):
    _response = await QuestionManager.get_question_by_id(request,id)
    return send_response({'message': json.dumps(
        _response, indent=4, sort_keys=True, default=str)})


@question_validate()
@question_details.route("/create", methods=["POST"])
async def create_question(request):
    payload = request.json
    payload = await QuestionManager.create_question(request,payload)
    return send_response({"message": json.dumps(
        payload, indent=4, sort_keys=True, default=str)})
