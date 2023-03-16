#!/usr/bin/env python
from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.models import User, Post
from config import Config
from app.auth.forms import RegistrationForm, OneTimeLinkForm, OTPForm, VerificationForm
from flask import current_app, url_for


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    ELASTICSEARCH_URL = None


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['SERVER_NAME'] = 'localhost.5000'
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()
        

        

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_OTP_page(self):
        response = self.client.get(url_for('auth.otp_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'OTP' in response.data)

    def test_valid_otp(self):
        u = User(username='testuser', email='test@example.com')
        u.set_password('testpassword')
        db.session.add(u)
        db.session.commit()

        response = self.client.post(url_for('auth.otp_login'), data={
            'username': 'testuser',
            'OTP': '1234'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Hi, testuser!' in response.data)
        

    def test_invalid_otp(self):
        u = User(username='testuser', email='test@example.com')
        u.set_password('testpassword')
        db.session.add(u)
        db.session.commit()

        response = self.client.post(url_for('auth.otp_login'), data={
            'username': 'testuser',
            'OTP': '12345'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Invalid OTP' in response.data)




    def test_verification_page(self):
        response = self.client.get(url_for('auth.verificationLink'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'One Time Verification' in response.data)

    def test_valid_verification(self):
        u = User(username='testuser', email='test@example.com')
        u.set_password('testpassword')
        db.session.add(u)
        db.session.commit()

        response = self.client.post(url_for('auth.verificationLink'), data={
            'username': 'testuser',
            'email': 'test@example.com'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Hi, testuser!' in response.data)
        

    def test_invalid_verification(self):
        u = User(username='testuser', email='test@example.com')
        u.set_password('testpassword')
        db.session.add(u)
        db.session.commit()

        response = self.client.post(url_for('auth.verificationLink'), data={
            'username': 'testuser',
            'email': 'wrong@example.com'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Invalid email' in response.data)




    def test_otl_page(self):
        response = self.client.get(url_for('auth.middle'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Comfirm Your One Time Link will be sent' in response.data)

    def test_valid_otl(self):
        u = User(username='testuser', email='test@example.com')
        u.set_password('testpassword')
        db.session.add(u)
        db.session.commit()

        response = self.client.post(url_for('auth.middle'), data={
            'username': 'testuser',
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'One Time link has been sent' in response.data)
        

    def test_invalid_otl(self):
        u = User(username='testuser', email='test@example.com')
        u.set_password('testpassword')
        db.session.add(u)
        db.session.commit()

        response = self.client.post(url_for('auth.middle'), data={
            'username': 'wrongtestuser',
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'Invalid username' in response.data)

    # def test_verification_form(self):
    #     u1 = User(username='testName3', email='test3@gmail.com')
    #     db.session.add(u1)
    #     db.session.commit()
    #     with self.app.test_request_context(method='POST'):
    #         # length less than 8
    #         form1 = VerificationForm(data={
    #             'username': 'testName3',
    #             'email': 'test3@gmail.com',
    #         })
    #         self.assertTrue(form1.validate())
    #         form2 = VerificationForm(data={
    #             'username': 'testName2',
    #             'email': 'test3@gmail.com',
    #         })
    #         self.assertFalse(form2.validate())
    #         form3 = VerificationForm(data={
    #             'username': 'testName3',
    #             'email': 'test@gmail.com',
    #         })
    #         self.assertFalse(form3.validate())


if __name__ == '__main__':
    unittest.main(verbosity=2)
