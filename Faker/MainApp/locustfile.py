import random
from locust import HttpLocust, TaskSet, task,seq_task,TaskSequence
from pyquery import PyQuery
import socket
#import locust_grafana
#locust_grafana.setup_graphite_communication()

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        self.client.post("/login", {"username":"ellen_key", "password":"education"})
        #print(assert response.status_code is 200, "Unexpected response code: " + response.status_code)
        #s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #s.connect(("www.facebook.com/login",443))
        #print("receiving data")
        #data = s.recv(1024)
        #print("data = ",(data))
        #print("response:",response.content)


    def logout(self):
        self.client.get("/logout", {"username":"ellen_key", "password":"education"})
    """@task(7)
    def role(self):
        self.client.post("/addroles")
    @task(6)
    def get(self):
        self.client.get("/category")
    @task(5)
    def news(self):
        self.client.post("/news")"""
    @task(4)
    def category(self):
	    self.client.post("/pages/feed")
    @task(3)
    def signup(self):
	    self.client.post("/marketplace")
    @task(2)
    def index(self):
        self.client.post("/events")
    @task(1)
    def profile(self):
        request=self.client.get("/profile")
        #pq = PyQuery(request.content)
        #print("profiles data:",pq)
        #print("Response status code:", request.status_code)
        #print("Response content:", request.content)



class categorieBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        self.client.post("/admin", {"username":"ellen_key", "password":"education"})

    def logout(self):
        self.client.post("/logout", {"username":"ellen_key", "password":"education"})

    @task(4)
    def category(self):
	    self.client.post("/apiaddcategories")
    @task(3)
    def signup(self):
	    self.client.get("/apiaddcarousel")
    @task(2)
    def index(self):
        self.client.get("/apiaddroles")
    @task(1)
    def profile(self):
        self.client.get("/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host ="http://www.facebook.com"
    weight=3
    #task_set = categorieBehavior
    wait_function = lambda self: random.expovariate(1)*1000

    #min_wait = 5000
    #max_wait = 9000
