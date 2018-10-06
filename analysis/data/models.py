from mongoengine import *
import mongoengine
from django.db import models



mongoengine.connect('test','mongodb://ram:Raghuram@9@localhost:27017')


class Address(Document):
    name = StringField(max_length =50)
    email = StringField(max_length=100)
    meta = {
      'indexes' :[
      'name',
      'email'
      ]
    }
