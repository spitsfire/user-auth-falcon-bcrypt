from mongoengine import *

class User(Document):
  uuid = StringField(required=True,unique=True,null=False)
  email = EmailField()
  password = StringField(required=True,null=False)