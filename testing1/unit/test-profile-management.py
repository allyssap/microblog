#!/usr/bin/env python
from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import User, Post
from config import Config
from app.main.forms import ChangePass
from app.main.forms import DeleteAccount


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


    def test_change_password_form_valid(self):
        u1 = User(username='testName1', email='test@gmail.com')
        u1.set_password('Testing1!')
        db.session.add(u1)
        db.session.commit()
        with self.app.test_request_context(method='POST'):
            form = ChangePass(data={
                'current_password' : 'Testing1!',
                'new_password': 'Testing2!',
                'confirm_password': 'Testing2!'
            })
            self.assertTrue(form.validate())


    def test_change_password_form_invalid(self):
        u1 = User(username='testName2', email='test2@gmail.com')
        u1.set_password('Testing1!')
        db.session.add(u1)
        db.session.commit()
        with self.app.test_request_context(method='POST'):
            # length less than 8
            form1 = ChangePass(data={
                'current_password' : 'Testing1!',
                'new_password': 'Test1!',
                'confirm_password': 'Test1!'
            })
            self.assertFalse(form1.validate())
            # no Capital letter
            form1 = ChangePass(data={
                'current_password' : 'Testing1!',
                'new_password': 'testing1!',
                'confirm_password': 'testing1!'
            })
            self.assertFalse(form1.validate())
            # no lower case letter
            form1 = ChangePass(data={
                'current_password' : 'Testing1!',
                'new_password': 'TESTING1!',
                'confirm_password': 'TESTING1!'
            })
            self.assertFalse(form1.validate())
            # no number
            form1 = ChangePass(data={
                'current_password' : 'Testing1!',
                'new_password': 'Testing!',
                'confirm_password': 'Testing!'
            })
            self.assertFalse(form1.validate())
            # no special character
            form1 = ChangePass(data={
                'current_password' : 'Testing1!',
                'new_password': 'Testing1',
                'confirm_password': 'Testing1'
            })
            self.assertFalse(form1.validate())


    def test_delete_user(self):
        u1 = User(username='testName1', email='test@gmail.com')
        u1.set_password('Testing1!')
        db.session.add(u1)
        db.session.commit()
        with self.app.test_request_context(method='POST'):
            # length less than 8
            form1 = DeleteAccount(data={
                'password' : 'Testing1!',
            })
            self.assertTrue(form1.validate())
        



if __name__ == '__main__':
    unittest.main(verbosity=2)
