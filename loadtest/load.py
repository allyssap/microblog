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
        self.app = create_app()
        self.client = self.app.test_client()
        self.context = self.app.test_request_context()
        self.context.push()
        db.init_app(self.app)
        db.create_all()
        with self.client as c:
            user = User(username=self.data["username"], email=self.data["email"]) ## need to be modified
            user.set_password(self.data["password"])
            db.session.add(user)
            db.session.commit()
            login_response = c.post('/api/login', data=json.dumps({"username":self.data["username"],"password":self.data["password"]}), headers={'Content-Type': 'application/json'})
            if login_response.status_code != 200:
                print('Login failed')
            else:
                print('login success')
            token_response = self.client.post('/api/tokens', auth=(self.data["username"], self.data["password"]))
            if token_response.status_code != 200:
                print('token failed')
            else:
                token_dict = login_response.json()
                self.token = token_dict['token']
            
    def on_stop(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()

    @task
    def login(self):
        #print(self.response.status_code)
        print(self.token)
        self.environment.runner.quit()
                