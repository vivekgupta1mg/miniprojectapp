from sanic import Sanic, Blueprint
from sanic.exceptions import SanicException
from torpedo import Request, send_response
from pydantic import ValidationError
from ..validation.check_payload import Check

so_basictest = Blueprint("so_basictest", version=4)


@so_basictest.route("/so_basictest/", methods=["POST"])
async def check(request: Request):

    payload = request.json
# validate payload data
    try:
        Check(**payload)
    except ValidationError:
       raise SanicException("Request data not correct.", status_code=400)
    return send_response({"message": payload})
