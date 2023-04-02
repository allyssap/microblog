from locust import HttpUser, between, task
import json
from app import create_app, db

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
            "password" : "TestPass01$",
        }        
        self.app = create_app()
        self.client = self.app.test_client()
        self.context = self.app.test_request_context()
        self.context.push()
        db.init_app(self.app)
        db.create_all()
        with self.client as c:
            register_response = c.post('/api/users', data=json.dumps(self.data), headers={'Content-Type': 'application/json'})
            if register_response.status_code != 201:
                print(register_response.status_code)
                raise Exception('Registration failed')
            login_response = c.post('/api/login', data=json.dumps(self.cred), headers={'Content-Type': 'application/json'})
            if login_response.status_code != 200:
                raise Exception('Login failed')
            #login_response = self.client.post('/api/tokens', auth=(self.data["username"], self.data["password"]))
            #if login_response.status_code != 200:
            #    raise Exception('Login failed')
            #else:
            #    self.token = login_response.json()['token']

    def on_stop(self):
        db.session.remove()
        db.drop_all()
        self.context.pop()

    @task
    def profile(self):
        print("\nFFFFFFFFFFFFFFFFUUUUUUUUUUUUUUUUUUUUCCCCCCCCCCCKKKKKKKKKKKKKKKK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
        '''
        with self.client as c:
            headers = {'Authorization': 'Bearer ' + self.token}
            user = self.data["username"]
            response = c.get(f'api/user/{user}', headers=headers)
            if response.status_code == 201:
                print(response.status_code, ": profile page task successful")
            else:
                print(response.status_code, ": profile page task failed")
                '''
        self.environment.runner.quit()
                