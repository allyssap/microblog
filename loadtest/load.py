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
        self.app = create_app()
        self.client = self.app.test_client()
        self.context = self.app.test_request_context()
        self.context.push()
        db.init_app(self.app)
        db.create_all()
        self.user = 'Test'
        self.email = 'test@gmail.com'
        self.passw = 'TestPass01$'
        user = User(username=self.user, email=self.email) ## need to be modified
        user.set_password(self.passw)
        db.session.add(user)
        db.session.commit()

    def on_stop(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()

    def get_csrf_token(self, response):
        soup = BeautifulSoup(response.get_data(as_text=True), 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrf_token'})['value']
        return csrf_token

    @task
    def login(self):
        with self.context:
            temp = User.query.filter_by(username=self.user).first()
            print(temp.__repr__())
            self.environment.runner.quit()
                