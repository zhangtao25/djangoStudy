from django.db import models

# Create your models here.
from mongoengine import Document, StringField

class User(Document):
    user_id = StringField()
    user_email = StringField()
    user_password = StringField()
    user_vcode_date = StringField()
    user_vcode = StringField()
    user_islive = StringField()