from locust import HttpUser, between, task, events
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
            "email" : "test@gmail.com"
        }
        self.loginFlag = False
        self.app = create_app()
        self.client = self.app.test_client()
        self.context = self.app.test_request_context()
        self.context.push()
        db.init_app(self.app)
        db.create_all()
        with self.client as c:
            register_response = c.post('/api/users', data=json.dumps(self.data), headers={'Content-Type': 'application/json'})
            if register_response.status_code != 201:
                print("Registration failed: ", register_response.status_code)
            else:
                print("registration success")
            token_response = c.post('/api/tokens', auth=(self.data["username"], self.data["password"]))
            if token_response.status_code != 200:
                print('login failed')
            else:
                self.loginFlag = True
                token_dict = token_response.json
                self.token = token_dict['token']
            
    def on_stop(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()

    @task(1)
    def profile(self):
        with self.client as c:
            if self.loginFlag == True:
                print(self.token)
                headers = {'Authorization': 'Bearer ' + self.token}
                user = self.data["username"]
                response = c.get(f'api/user/{user}', headers=headers)
                if response.status_code == 201:
                    response.success()
                    #events.request_success.fire(request_type="GET", name=f'api/user/{user}', response_time=response.elapsed.total_seconds(), response_length=len(response.content))
                    #print(response.status_code, ": profile page task successful")
                else:
                    response.failure(response.status_code)
                    #events.request_failure.fire(request_type="GET", name=f'api/user/{user}', response_time=response.elapsed.total_seconds(), exception=None)
                    #print(response.status_code, ": profile page task failed")
                