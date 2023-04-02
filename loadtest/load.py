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
        self.login = {
            "username" : "Test",
            "password" : "TestPass01$",
        }
        self.app = create_app()
        self.client = self.app.test_client()
        self.context = self.app.test_request_context()
        self.context.push()
        db.init_app(self.app)
        db.create_all()
        with self.client as c:
            c.post('/api/users', data=json.dumps(self.data), headers={'Content-Type': 'application/json'})
            self.response = c.post('/api/login', data=json.dumps(self.login), headers={'Content-Type': 'application/json'})

    def on_stop(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()

    @task
    def login(self):
        print(self.response.status_code)
        self.environment.runner.quit()
                