from torpedo.db import CITextField, CustomTextField
from tortoise import Model, fields


class AbstractBaseUser(Model):
    """
    Abstract Class for User and Guest User Models
    Provides all the fields for User Tables

    """

    serializable_keys = {
        "username",
        "password",
        "email",
        "updated_on",
        "created_on",


    }

    username = CITextField(max_length=100, unique=True)
    password = fields.CharField(max_length=100, null=True)
    email = CITextField(max_length=100, unique=True, null=True)
    created_on = fields.DateField(auto_now_add=True)
    updated_on = fields.DateField(auto_now=True, null=True)

    class Meta:
        abstract = True
