import random
from locust import HttpLocust, TaskSet, task,seq_task,TaskSequence

with open('/home/hp/abc.txt','r') as f:
     words = [line.rstrip('\n') for line in f]



class searchbehaviour(TaskSet):
    @task(1)
    def search(self):
         word = words[random.randint(0,len(words)-2)]
         print("wordlist:",word)
         length = random.randint(2,len(word))
         self.client.get("/search/?q=%s" % word[0:length])
class HttpSession(TaskSet):
    @task
    def post_img(self):
    #headers = {'1': '1', '2': '2'}
        test_file = '/home/hp/Documents/book.jpeg'
        self.client.request('POST', '/upload', files={'file': open(test_file, 'rb')})#, headers=headers)




class WebsiteUser(HttpLocust):
        host = 'https://imgbb.com'
        task_set = HttpSession
        min_wait = 100
        max_wait = 300



class websiteBehaviour(HttpLocust):
    host="https://www.bing.com"
    task_set = searchbehaviour
    wait_function = lambda self: random.expovariate(1)*1000
