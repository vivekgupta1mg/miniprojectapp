from collections import defaultdict

from torpedo.db import CustomTextField, ModelUtilMixin
from tortoise import Model, fields
from .abc import AbstractBaseUser


class Users(AbstractBaseUser, ModelUtilMixin):
    force_password_reset = fields.BooleanField(null=True)
    is_login = fields.BooleanField(null=True, DEFAULT=False)

    @property
    def external_id(self):
        return ""

    class Meta:
        table = "users"

    async def to_dict(self, filter_keys=None, get_related=True, related_fields=None):
        result = await super().to_dict(filter_keys, get_related, related_fields)
        return result




