from torpedo import Request, send_response
from sanic import Blueprint, Sanic
from sanic.response import json
from ..managers.comment import CommentManager
from pydantic import ValidationError
from ..validation.check_payload import Check
from ..decorators.comment import  comment_validate
import json


comment_details = Blueprint(
    "comment_details", url_prefix="/comment_details", version=4)


@comment_validate()
@comment_details.route("/", methods=["GET"])
async def show_comment(request):
    _response = await CommentManager.get_comments(request)
    return send_response({'message': json.dumps(
        _response, indent=4, sort_keys=True, default=str)})

@comment_validate()
@comment_details.route("/<id:int>", methods=["GET"])
async def show_comment_by_id(request, id):
    _response = await CommentManager.get_comment_by_id(request, id)
    return send_response({'message': json.dumps(
        _response, indent=4, sort_keys=True, default=str)})


@comment_validate()
@comment_details.route("/create", methods=["POST"])
async def create_comment(request):
    payload = request.json
    payload = await CommentManager.create_comment(request,payload)
    return send_response({"message": json.dumps(
        payload, indent=4, sort_keys=True, default=str)})
