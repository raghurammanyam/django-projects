from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType,Text,Date,Search
from . import models
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
import time
from MainApp.models  import Document

connections.create_connection()




class DocumentIndex(indexes.SearchIndex, indexes.Indexable):
    name = indexes.CharField(document=True, use_template=True)
    text = indexes.CharField(model_attr='text')
    posted_date = indexes.DateTimeField(model_attr='posted_date')

    def get_model(self):
        return Document

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(posted_date__lte=datetime.datetime.now())

class DocumentIndex(DocType):
    name = Text()
    text = Text()
    posted_date = Date()

    class Meta:
        index = 'document-index'

    def bulk_indexing():
        DocumentIndex.init()
        es = Elasticsearch()
        bulk(client=es, actions=(b.indexing() for b in models.Document.objects.all().iterator()))

        print("bulkdata:",bulk)
        #time.sleep(0.1)
def search(author):
    s=Search().filter('term',name=author)
    response = s.execute()
    return response
