from torpedo import Request, send_response
from sanic import Blueprint, Sanic
from sanic.response import json
from ..managers.answer import AnswerManager
from pydantic import ValidationError
from ..validation.check_payload import Check
from ..decorators.answer import  answer_validate
import json 
answer_details = Blueprint(
    "answer_details", url_prefix="/answer_details", version=4)




@answer_validate()
@answer_details.route("/", methods=["GET"])
async def show_answer(request):
    _response = await AnswerManager.get_answers(request)
    return send_response({'message': json.dumps(
        _response, indent=4, sort_keys=True, default=str)})

@answer_validate()
@answer_details.route("/<id:int>", methods=["GET"])
async def show_answer_by_id(request, id):
    
    _response = await AnswerManager.get_answer_by_id(request, id)
    return send_response({'message': json.dumps(
        _response, indent=4, sort_keys=True, default=str)})


@answer_validate()
@answer_details.route("/create", methods=["POST"])
async def create_answer(request):
    payload = request.json
    payload = await AnswerManager.create_answer(request, payload)
    return send_response({"message": json.dumps(
        payload, indent=4, sort_keys=True, default=str)})
