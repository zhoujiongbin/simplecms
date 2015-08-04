from django.db import models
from admin.cat.models import Cat

class Article(models.Model):
    article_title = models.CharField(max_length=200)
    publish_time = models.DateTimeField(auto_now_add=True)
    article_author = models.CharField(max_length=50)
    article_content = models.TextField()
    article_cat_id = models.ForeignKey(Cat)
