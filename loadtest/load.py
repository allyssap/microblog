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
        user = User(username='Test', email='testasdfg@gmail.com') ## need to be modified
        user.set_password('TestPass01$')
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
            with self.client as c:
                form = LoginForm()
                form.username.data = 'Test'
                form.username.data = 'TestPass01$'
                #csrf_token = self.get_csrf_token(c.get('/auth/login'))
                #json.dumps({'username': 'Test1', 'password': 'TestPass01$', '_csrf_token': str(csrf_token)})
                #headers = {'X-CSRF-TOKEN': str(csrf_token)}
                response = c.post('/auth/login', data=form.data, headers={})
                if response.status_code == 200:
                    print('\t\t\tplease, I beg you!')
                    #print(csrf_token)
                    #print(response.get_data(as_text=True))
                    #self.environment.runner.quit()
                else:
                    print('Login Unsuccessful')
                    response.failure('failed')
        '''
        with self.client.post('/auth/login', data=json.dumps({'username': 'Test9', 'password': 'TestPass01$'}),
                        headers={},
                        name='Test 0',
                        catch_response=True
        ) as response:
            if response.status_code == 200:
                print(response.status_code)
                response.success()
            else:
                response.failure('failed')
        '''
                