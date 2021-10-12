from torpedo.exceptions import BadRequestException
from torpedo.wrappers import ORMWrapper
from ...caches import UserCache
from ...models import Users
from ..app import Base as DB
from datetime import datetime


class UserManager:
    @classmethod
    async def get_user(cls, payload):
        username = payload.get("username")

        user = await UserCache.get(username)
        if user:
            return user
        else:
            user = await ORMWrapper.get_by_filters(Users, {"username": username})
            if not user:
                raise BadRequestException("No users found.")
            user = await user[0].to_dict()

            # set value to cache
            await UserCache.set_user(username, user)
            return user

    @classmethod
    async def create_user(cls, payload):
        payload["created_on"] = datetime.now()
        user = await DB.create_instance(Users, payload)
        print(user)
        return user

    @classmethod
    async def verify_login(cls, payload):
        user = await DB.verify_details(Users, payload)
        return user

    @classmethod
    async def update_field(cls, payload):
        id = payload['username']
        del payload['username']
        user = await DB.update(Users, payload)
        return user

    @classmethod
    async def get_user_by_id(cls, payload):
        user = await Users.get(id=1)
        print(user)
        return user
