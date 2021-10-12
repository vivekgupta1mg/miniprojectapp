from torpedo.wrappers import ORMWrapper
from tortoise.functions import Max
from ...models import Users


class Base(ORMWrapper):

    @classmethod
    async def create_instance(cls, model, data):
        print(data)
        row = await cls.create(model, data)
        return row

    @classmethod
    async def verify_details(cls, model, data):
        row = await cls.get_by_filters(model, data)
        return row

    @classmethod
    async def update(cls, model, data):
        row = await cls.update_with_filters(None, model, data, where_clause={'email': data['email']})
        print(row)
        return row

    @classmethod
    async def update_question(cls, model, data):
        id = data['id']
        del data['id']
        row = await cls.get_by_filters(model, data)
        return row

    @classmethod
    async def update_question(cls, model, data):
        id = data['id']
        del data['id']
        row = await cls.update_with_filters(None, model, data, where_clause={'id': id})
        return row


    @classmethod
    async def get_question(cls):
        row = await cls.raw_sql('''select * from question''')
        return row
    
    @classmethod
    async def get_question_by_id(cls, model, data):
        row = await cls.get_by_filters(model, data)
        return row

    @classmethod
    async def delete_question(cls, model, data):
        row = await cls.raw_sql('''delete from question where id=''' + data['id'])
        return row


    @classmethod
    async def get_answer(cls):
        row = await cls.raw_sql('''select * from answer''')
        return row
        
    @classmethod
    async def update_answer(cls, model, data):
        id = data['id']
        del data['id']
        row = await cls.update_with_filters(None, model, data, where_clause={'id': id})
        return row


    @classmethod
    async def get_answer_by_id(cls, model, data):
        row = await cls.raw_sql('''select * from answer where id=''' + data['id'])
        return row


    @classmethod
    async def delete_answer(cls, model, data):
        row = await cls.raw_sql('''delete from answer where id=''' + data['id'])
        return row

    @classmethod
    async def get_comment(cls):
        row = await cls.raw_sql('''select * from comment''')
        return row


    @classmethod
    async def update_comment(cls, model, data):
        id = data['id']
        del data['id']
        row = await cls.update_with_filters(None, model, data, where_clause={'id': id})
        return row


    @classmethod
    async def delete_comment(cls, model, data):
        row = await cls.raw_sql('''delete from comment where id=''' + data['id'])
        return row
