from django.db import models
from .search import DocumentIndex



class Document(models.Model):
    name = models.CharField(max_length = 122)
    text = models.TextField()
    posted_date = models.DateTimeField(blank=True,null=True)
    def indexing(self):
        obj = DocumentIndex(
             meta ={'id':self.id},
             name = self.name,
             text = self.text,
             posted_date=self.posted_date
        )
        obj.save()
        return obj.to_dict(include_meta=True)
