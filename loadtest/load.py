from locust import HttpUser, between, task, SequentialTaskSet
import json
from app.auth.forms import LoginForm
from app import create_app, db
from flask import url_for
from app.models import User
from bs4 import BeautifulSoup

class MicroUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://localhost:5000"

    def on_start(self):
        self.data = {
            "username" : "Test",
            "password" : "TestPass01$",
            "email" : "example@gmail.com"
        }
        self.cred = {
            "username" : "Test",
            "password" : "TestPass02S$",
        }
        self.app = create_app()
        self.client = self.app.test_client()
        self.context = self.app.test_request_context()
        self.context.push()
        db.init_app(self.app)
        db.create_all()
        with self.client as c:
            c.post('/api/users', data=json.dumps(self.data), headers={'Content-Type': 'application/json'})
            login_response = c.post('/api/login', data=json.dumps(self.cred), headers={'Content-Type': 'application/json'})
            if login_response.status_code == 200:
                self.session.cookies.update(login_response.cookies)
            else:
                raise Exception('Login failed')

    def on_stop(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()

    @task
    def profile(self):
        with self.client as c:
            profile_route = '/user' + self.data["username"]
            response = c.get(profile_route, headers={'Cookie': self.session.cookies.output(header='', sep=';')})
            if response.status_code == 200:
                print(response.status_code, ": profile page task successful")
            else:
                print(response.status_code, ": profile page task failed")
        self.environment.runner.quit()
                