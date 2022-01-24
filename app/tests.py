from flask_testing import TestCase
from app import create_app, Configuration
from models import db, User
from flask import url_for


class TestConfiguration(Configuration):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/names.db'
    TESTING = True
    DEBUG = True


class TestBase(TestCase):

    def create_app(self):
        app = create_app(TestConfiguration)

        return app

    def setUp(self):
        db.drop_all()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_index(self):
        response = self.client.get(url_for('main.index'))
        self.assertEqual(response.status_code, 200)

    def test_say(self):
        response = self.client.post(
            url_for('main.say_hi'),
            data={'name': 'Олег'}
        )
        self.assertIn('Привіт, Олег', response.data.decode("utf-8"))

        response = self.client.post(
            url_for('main.say_hi'),
            data={'name': 'Олег'}
        )
        self.assertIn('Вже бачилися, Олег', response.data.decode("utf-8"))

    def test_names(self):
        response = self.client.post(
            url_for('main.say_hi'),
            data={'name': 'Олег'}
        )
        self.assertIn('Привіт, Олег', response.data.decode("utf-8"))

        response = self.client.get(
            url_for('main.list_names'),
            data={'name': 'Олег'}
        )
        self.assertIn('Вже бачилися з', response.data.decode("utf-8"))
        self.assertIn('Олег', response.data.decode("utf-8"))
