from flask_testing import TestCase
from application.app import app, db
from application.models import User
import os
from setup import basedir
import json


class BaseTestConfig(TestCase):
    default_user = {
        "email": "default@gmail.com",
        "password": "something2"
    }

    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app

    def setUp(self):
        self.app = self.create_app().test_client()
        # db.create_all()
        res = self.app.post(
                "/api/create_user",
                data=json.dumps(self.default_user),
                content_type='application/json'
        )

        self.token = json.loads(res.data.decode("utf-8"))["token"]

    def tearDown(self):
        # db.connection.drop_database('demo_db')
        # db.drop_database('demo_db')
        try:
            db.connection.drop_database('demo_db')
        except:
            db.connection.client.drop_database('demo_db')
