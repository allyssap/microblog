from locust import HttpUser, between, task, events
import json
import time
import psutil
from app import create_app, db
from collect import consumption
import uuid
from app.models import User

class MicroUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://localhost:5000"

    def on_start(self):
        self.monitoring_task = self.environment.runner.greenlet.spawn(self.monitor_performance)

        unique_username = "TestUser_" + str(uuid.uuid4())
        self.start_memory_usage = psutil.virtual_memory().used

        self.data = {
            "username" : unique_username,
            "password" : "TestPass01$",
            "email" : unique_username + "@gmail.com"
        }        
  
        self.header = None
        self.app = create_app()
        self.client = self.app.test_client()
        self.context = self.app.test_request_context()
        self.context.push()
        db.init_app(self.app)
        db.create_all()
        with self.client as c:
            home_response = c.get('/api/home', headers={})
            if home_response.status_code == 200:
                register_response = c.post('/api/users', data=json.dumps(self.data), headers={'Content-Type': 'application/json'})
                if register_response.status_code != 201:
                    pass
#                    print("Registration failed: ", register_response.status_code)
                else:
#                    print("Registration success")
                    otp_response = c.post('/api/otp', data=json.dumps({"username":self.data["username"], "otp":'1234'}), headers={'Content-Type': 'application/json'})
                    if otp_response.status_code == 201:
 #                       print("OTP verification successful")
                        token_response = c.post('/api/tokens', auth=(self.data["username"], self.data["password"]), headers={'Content-Type': 'application/json'})
                        if token_response.status_code != 200:
  #                          print('Credentials invalid')
                            pass
                        else:
   #                         print('Credentials valid')
                            token = token_response.json['token']
                            self.header = {'Authorization': 'Bearer ' + token}
                            index_response = c.get('/api/index', data=json.dumps({"username":self.data["username"]}) ,headers={'Content-Type': 'application/json', 'Authorization': self.header["Authorization"]})
       #                     if index_response.status_code == 200:
    #                            print('Login successful')
      #                      else:
     #                           print('Login unsuccessful')         
            
    def on_stop(self):
        db.session.remove()
        user_to_delete = User.query.filter_by(username=self.data["username"]).first()
        if user_to_delete:
            db.session.delete(user_to_delete)
            db.session.commit()


    def monitor_performance(self):
        while True:
            self.collect_stats()
            time.sleep(5)

    def collect_stats(self):
        stats = self.environment.runner.stats
        total_requests = stats.total.num_requests
        avg_response_time = stats.total.avg_response_time
        min_response_time = stats.total.min_response_time
        max_response_time = stats.total.max_response_time
        error_rate = stats.total.fail_ratio
        #cpu_percent = psutil.cpu_percent()
        #memory_usage = psutil.virtual_memory().used
        #consumption(psutil.cpu_percent(), psutil.virtual_memory().used)
        # Write the data to the Locust web interface
        data = {
            "total_requests": total_requests,
            "avg_response_time": avg_response_time,
            "min_response_time": min_response_time,
            "max_response_time": max_response_time,
            "error_rate": error_rate
            #"cpu_percent": cpu_percent,
            #"memory_usage": memory_usage
        }
        self.environment.events.report_to_master(json.dumps(data))
        # Remove the comment from the next one to output data struct to console
        # print(json.dumps(data))

    @task(1)
    def profile(self):
        with self.client as c:
            if self.header is not None:
                start_time = time.time()
#                print(self.header)
                #headers = {'Authorization': 'Bearer ' + self.token}
                user = self.data["username"]
                response = c.get(f'api/user/{user}', headers=self.header)
                response_time = int((time.time() - start_time) * 1000)
                if response.status_code == 201:
                    self.environment.events.request.fire(request_type="GET", name=f'api/user/{user}', response_time=response_time, response_length=len(response.get_data().decode()))
 #                   print(response.status_code, ": profile page task successful")
                else:
                    self.environment.events.request.fire(request_type="GET", name=f'api/user/{user}', response_time=response_time, exception=None)
  #                  print(response.status_code, ": profile page task failed")
                
                megabytes = round(psutil.virtual_memory().used / (1024 * 1024), 2)
                cpu_percent = psutil.cpu_percent()
                consumption(self.environment.runner.stats.total.num_requests - 1, cpu_percent, megabytes)
                
