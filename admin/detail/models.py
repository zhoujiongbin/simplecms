from django.db import models

# Create your models here.

class Detail(models.Model):
    logo_path = models.URLField()
    title = models.CharField(max_length=200)
    introduction = models.TextField()
