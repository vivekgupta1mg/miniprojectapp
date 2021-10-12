from sanic import Blueprint, Sanic
import sanic
from sanic.response import json
from unittest import TestCase
import unittest
from app.routes import so_basictest


app = Sanic(__name__)
app.blueprint(so_basictest)


class TestValidation(TestCase):
    def test_1(self):
        data = {"name": "vivek", "address": "vigyan nagar", "id": 1}
        request, response = app.test_client.post('/v4/so_basictest/', json=data,
                                                 headers={"Content-Type": "application/json"})
        assert response.status == 200



if __name__ == "__main__":
    unittest.main()
