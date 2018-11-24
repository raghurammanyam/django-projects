from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
#from . import models
from haystack import indexes
from haystack.query import SearchQuerySet
from MainApp.models import BlogPost

# Create a connection to ElasticSearch
connections.create_connection()
#import haystack
#haystack.autodiscover()

# ElasticSearch "model" mapping out what fields to index
class BlogPostIndex(indexes.SearchIndex, indexes.Indexable):
    author = indexes.EdgeNgramField(document=True,model_attr='author')
    posted_date = Date(model_attr='pub_date')
    title = indexes.EdgeNgramField(model_attr='title')
    text = indexes.EdgeNgramField(document=True)
    def get_model(self):
        return BlogPost
    def index_queryset(self, using=None):
        return self.get_model().objects.all()



# Bulk indexing function, run in shell
    def bulk_indexing():
        #BlogPostIndex.init()
        es = Elasticsearch()
        a=bulk(client=es, actions=(b.indexing() for b in models.BlogPost.objects.all().iterator()))
        return a

# Simple search function
def search(author):
    s = SearchQuerySet().filter(
        author=author).models(BlogPost)

        #Search().filter('match', author= u'%s*' )
    print("bjbsj:",s)        #response = s.execute()
    return s

def indexing(self):
   obj = BlogPostIndex(
     meta={'id': self.id,'author':self.author,
     'posted_date':self.posted_date,
     'title':self.title,
     'text':self.text}
   )
   obj.save()
   return obj.to_dict(include_meta=True)
