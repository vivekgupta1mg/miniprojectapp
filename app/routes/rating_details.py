from torpedo import Request, send_response
from sanic import Blueprint, Sanic
from sanic.response import json
from ..managers.rating import RatingManager
from pydantic import ValidationError
from ..validation.check_payload import Check
from ..decorators.rating import rating_validate
import json


rating_details = Blueprint("rating_details", url_prefix="/rating_details", version=4)




@rating_validate()
@rating_details.route("/", methods=["GET"])
async def show_rating(request):
    _response = await RatingManager.get_ratings(request)
    return send_response({'message': json.dumps(
        _response, indent=4, sort_keys=True, default=str)})



@rating_validate()
@rating_details.route("/<id:int>", methods=["GET"])
async def show_rating_by_id(request, id):
    _response = await RatingManager.get_rating_by_id(request, id)
    return send_response({'message': json.dumps(
        _response, indent=4, sort_keys=True, default=str)})



@rating_validate()
@rating_details.route("/create", methods=["GET"])
async def create_rating(request):
    _response = await RatingManager.create_rating(request)
    return send_response({"message": json.dumps(
        _response, indent=4, sort_keys=True, default=str)})
