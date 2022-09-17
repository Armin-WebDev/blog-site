from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    #auther
    # #cover = models.ImageField()
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    #category 
    class Meta:
        ordering =  ['-created_at']

    def __str__(self) :
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='media',blank=True)
    description = models.CharField(max_length=320)

    def __str__(self):
        return f'{self.user.first_name + " " + self.user.last_name} '



