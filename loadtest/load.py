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
        self.username = 'Test'
        self.passw = 'TestPass01$'
        self.email = 'test@gmail.com'
        self.app = create_app()
        self.client = self.app.test_client()
        self.context = self.app.test_request_context()
        self.context.push()
        with self.client as c:
            self.response = c.post('/api/users', data={"username": str(self.username), "password": str(self.passw), "email": str(self.email)})
            
    def on_stop(self):
        self.context.pop()

    @task
    def login(self):
        print(self.response.status_code)
        self.environment.runner.quit()
                