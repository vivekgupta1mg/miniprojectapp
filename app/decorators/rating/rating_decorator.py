from functools import wraps
from sanic.response import json
from ...validation.check_payload import Check
from pydantic import ValidationError, validator
from ...constants import ErrorMessages

# from managers.user import UserManager
# from .user_decorator import user_validate
from torpedo.exceptions import BadRequestException
from torpedo.wrappers import ORMWrapper





def rating_validate():
    def decorator(f):
        @wraps(f)
        async def validate(self,request, *args, **kwargs):
            # run some method that checks the request
            # for the client's authorization status
            is_validate= Check(request)

            if is_validate:
                # the user is authorized.
                # run the handler method and return the response
                response = await f(request, *args, **kwargs)
                return response
            else:
                # the user is not authorized. 
                raise BadRequestException(ErrorMessages.FIELD_REQUIRED.value.format(key=id))
        return validate
    return decorator



