
import uuid
from torpedo.db import CustomTextField, ModelUtilMixin
from enum import Enum, IntEnum
from tortoise.models import Model
from tortoise import Model, fields
from datetime import datetime





class EntityType(int,Enum):
    question = 1
    answer = 2




# class AbstractBasePrescription(Model):

#  serializable_keys = {'id', 'username', 'email', 'password'}

# class Users(Model, ModelUtilMixin):
#     id = fields.BigIntField(pk=True)
#     username = fields.TextField(null=True)
#     email = fields.CharField(max_length=50)
#     password = fields.CharField(max_length=50)

#     class Meta:
#         table = 'users'


class Questions(Model, ModelUtilMixin):
    id = fields.BigIntField(pk=True)
    user = fields.ForeignKeyField(
        'sanic_3.Users', related_name='user_id', on_update=fields.CASCADE,)
    question_text = fields.TextField()
    description = fields.TextField(null=True)
    answered = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'questions'


class Answers(Model,ModelUtilMixin):
    id = fields.BigIntField(pk=True)
    question = fields.ForeignKeyField(
        'sanic_3.Questions', related_name='question_id', on_update=fields.CASCADE,)
    user = fields.ForeignKeyField(
        'sanic_3.Users', related_name='user_aid', on_update=fields.CASCADE,)
    votes = fields.BigIntField()
    answer_text = fields.TextField()
    accepted = fields.BooleanField(default=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'answers'


class Ratings(Model, ModelUtilMixin):
    id = fields.BigIntField(pk=True)
    user = fields.ForeignKeyField(
        'sanic_3.Users', related_name='user_rid', on_update=fields.CASCADE,)
    question = fields.ForeignKeyField(
        'sanic_3.Questions', related_name='question_rid', on_update=fields.CASCADE,)
    answer = fields.ForeignKeyField(
        'sanic_3.Answers', related_name='answer_rid', on_update=fields.CASCADE,)
    rating_star = fields.BigIntField()

    class Meta:
        table = 'ratings'


class Comments(Model, ModelUtilMixin):
    id = fields.BigIntField(pk=True)
    user = fields.ForeignKeyField(
        'sanic_3.Users', related_name='user_cid', on_update=fields.CASCADE,)
    answer = fields.ForeignKeyField(
        'sanic_3.Answers', related_name='answer_id', on_update=fields.CASCADE,)
    question_entity = fields.ForeignKeyField(
        'sanic_3.Questions', related_name='question_eid', on_update=fields.CASCADE,)
    answer_entity = fields.ForeignKeyField(
        'sanic_3.Answers', related_name='answer_eid', on_update=fields.CASCADE,)
    entity_type = fields.IntEnumField(EntityType, description="entity_type")
    comment_text = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'comments'
