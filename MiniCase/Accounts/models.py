from django.db import models
from django.db.models import CharField
from django.db.models import EmailField

class User(models.Model):
    username = CharField(max_length=25)

    def __str__(self):
        return self.username
