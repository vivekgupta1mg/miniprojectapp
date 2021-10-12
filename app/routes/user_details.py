from re import U
from torpedo import Request, send_response
from sanic import Blueprint, Sanic
from sanic.response import json
from ..managers.user import UserManager
from pydantic import ValidationError
from ..decorators.user import user_validate
from ..validation.check_payload import Check
import json


user_details = Blueprint(
    "user_details", url_prefix="/user_details", version=4)




@user_validate()
@user_details.route("/add-user", methods=["POST"])
async def signup(request: Request):
    payload = request.json
    result = await UserManager.create_user(payload)
    if result:
        return send_response({'message': json.dumps(
            payload, indent=4, sort_keys=True, default=str)})
    else:
        return send_response({'message': "something went wrong"})


@user_validate()
@user_details.route("/login", methods=["POST"])
async def login(request: Request):
    payload = request.json
    result = await UserManager.verify_login(payload)
    if result:
        payload['is_login'] = True
        await UserManager.update_field(payload)

        return send_response({'message': "login successful"})
    else:
        return send_response({'message': "invalid credential"})



