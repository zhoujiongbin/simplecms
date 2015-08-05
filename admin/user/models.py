from django.db import models

# Create your models here.
from datetime import datetime

class User(models.Model):
    password  = models.BinaryField()
    account = models.CharField(max_length=20,unique=True)
    email = models.EmailField()
    power = models.IntegerField()
    joined_time = models.TimeField(default=datetime.now())
    last_login = models.TimeField(null=True)
