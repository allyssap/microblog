#!/usr/bin/env python
from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import User, Post
from config import Config
from app.auth.forms import RegistrationForm


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ELASTICSEARCH_URL = None


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_create_valid_user_form(self):
        with self.app.test_request_context(method='POST'):
            form = RegistrationForm(data={
                'username': 'testName1',
                'email': 'testuser@gmail.com',
                'password': 'Testing1!',
                'password2': 'Testing1!'
            })
            self.assertTrue(form.validate())

    def test_create_invalid_user_password(self):
        with self.app.test_request_context(method='POST'):
            # length less than 8
            form1 = RegistrationForm(data={
                'username': 'testName1',
                'email': 'testuser@gmail.com',
                'password': 'Test1!',
                'password2': 'Test1!'
            })
            self.assertFalse(form1.validate())
            # no Capital letter
            form1 = RegistrationForm(data={
                'username': 'testName1',
                'email': 'testuser@gmail.com',
                'password': 'testing1!',
                'password2': 'testing1!'
            })
            self.assertFalse(form1.validate())
            # no lower case letter
            form1 = RegistrationForm(data={
                'username': 'testName1',
                'email': 'testuser@gmail.com',
                'password': 'TESTING1!',
                'password2': 'TESTING1!'
            })
            self.assertFalse(form1.validate())
            # no number
            form1 = RegistrationForm(data={
                'username': 'testName1',
                'email': 'testuser@gmail.com',
                'password': 'Testing!',
                'password2': 'Testing!'
            })
            self.assertFalse(form1.validate())
            # no special character
            form1 = RegistrationForm(data={
                'username': 'testName1',
                'email': 'testuser@gmail.com',
                'password': 'Testing1',
                'password2': 'Testing1'
            })
            self.assertFalse(form1.validate())

    def test_repeat_user(self):
        u1 = User(username='testName1', email='test@gmail.com')
        db.session.add(u1)
        db.session.commit()
        with self.app.test_request_context(method='POST'):
            # length less than 8
            form1 = RegistrationForm(data={
                'username': 'testName1',
                'email': 'testuser@gmail.com',
                'password': 'Testing1!',
                'password2': 'Testing1!'
            })
            self.assertFalse(form1.validate())
            form2 = RegistrationForm(data={
                'username': 'testName2',
                'email': 'test@gmail.com',
                'password': 'Testing1!',
                'password2': 'Testing1!'
            })
            self.assertFalse(form2.validate())


if __name__ == '__main__':
    unittest.main(verbosity=2)
