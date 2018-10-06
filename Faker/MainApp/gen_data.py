from faker import Faker,Factory
from elasticsearch import Elasticsearch
import json
import time
ES_HOST = 'http://localhost:9200/'
es = Elasticsearch(ES_HOST)

number = 0

def create_name():
    for x in range(1000000):
        genName = fake.name()
        genJob = fake.job()
        genEmail = fake.address()
        genFun = fake.numerify('#######')
        print(genJob)
        global number
        number += 1

        go = es.index(
             index="search",
             doc_type="use",
             id = str(number),
             body={
                 "name":genName,
                 "job":genJob,
                 "email":genEmail,
                 "fff": genFun
             }
        )

        print (json.dumps(go))
        time.sleep(0.01)
if __name__ == '__main__':
    fake = Faker('IN')
    create_name()
