from datetime import datetime
from django.db import models

# Create your models here.


class Article(models.Model):
    #auther
    # #cover = models.ImageField()
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    #category 
