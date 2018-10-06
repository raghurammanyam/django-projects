from elasticsearch import Elasticsearch
from time import clock


ES_HOST = 'http://localhost:9200'
query = input("serach for people: \n")
#h=time.time()

if __name__ == '__main__':
    es = Elasticsearch(ES_HOST)
    start = clock()
    res = es.search(index="search",doc_type="use",body={"query":{"wildcard":{"_all":query}}},size=100)
    end=clock()
    time_taken =end-start
    print("%d documents found: "% res['hits']['total'],time_taken)
    for doc in res['hits']['hits']:
        #print("%s) %s <mailto:%s> %s %s" % (doc['_id'], doc['_source']['name'],doc['_source']['email'],doc['_source']['job'],doc['_source']['fff']))
        print (doc)
