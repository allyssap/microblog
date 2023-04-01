from locust import HttpUser, between, task, SequentialTaskSet
import json
from app.auth.forms import LoginForm
from app import create_app, db
from flask import url_for
from app.models import User

class MicroUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://localhost:5000"

    def on_start(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.context = self.app.app_context()
        self.context.push()
        db.init_app(self.app)
        db.create_all()

    def on_stop(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()

    @task
    def login(self):
        with self.client as c:
            user = User(username='Test', email='test@gmail.com') ## need to be modified
            user.set_password('TestPass01$')
            db.session.add(user)
            db.session.commit()
            form = LoginForm()
            form.username.data = 'Test'
            form.username.data = 'TestPass01$'
            response = c.post(url_for('auth.login'), data=form.data, allow_redirects=True)
            if response.status_code == 200:
                print(response.status_code)
                response.success()
            else:
                print('Login Unsuccessful')
                response.failure('failed')
        '''
        with self.client.post('/auth/login', data=json.dumps({'username': 'Test9', 'password': 'TestPass01$'}),
                        headers={},
                        name='Test 0',
                        catch_response=True
        ) as response:
            if response.status_code is 200:
                print(response.status_code)
                response.success()
            else:
                response.failure('failed')
                '''