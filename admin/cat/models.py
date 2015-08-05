from django.conf import settings
from django.db import models

# Create your models here.

class Cat(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=100)
    cat_father = models.IntegerField()
