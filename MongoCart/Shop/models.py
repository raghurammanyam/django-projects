from django.db import models
import mongoengine
from mongoengine import *
import datetime

#mongoengine.connect('Shop','mongodb://ram:Raghuram@9@localhost:27017')



class CustomersModel(EmbeddedDocument):
    name = StringField(max_length=200)
    Address = StringField(max_length=200)
    mobile_no = StringField(max_length=200)
    created = DateTimeField(default=datetime.datetime.now)
    updated = DateTimeField(default=datetime.datetime.now)

class CategoriesModel(EmbeddedDocument):
    name = StringField(max_length=200)
    status=BooleanField()
    created = DateTimeField(default=datetime.datetime.now)
    updated = DateTimeField(default=datetime.datetime.now)

class ItemsModel(EmbeddedDocument):
    name = StringField(max_length=200)
    categorie =ListField(EmbeddedDocumentField(CategoriesModel))
    price =DecimalField()
    status=BooleanField()
    Description = StringField(max_length=200)
    created = DateTimeField(default=datetime.datetime.now)
    updated = DateTimeField(default=datetime.datetime.now)


class OrdersModel(Document):
    user = ListField(EmbeddedDocumentField(CustomersModel))
    Item = ListField(EmbeddedDocumentField(ItemsModel))
    Total_price = DecimalField()
    status = BooleanField()
    created = DateTimeField(default=datetime.datetime.now)
    updated = DateTimeField(default=datetime.datetime.now)
















# Create your models here.
