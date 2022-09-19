from datetime import datetime
from operator import mod
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = 'avatars/',default='avatars/default.jpg' )
    description = models.CharField(max_length=320)

    def __str__(self):
        return f'{self.user.first_name + " " + self.user.last_name} '

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Article(models.Model):
    auther = models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True)
    cover = models.ImageField(upload_to = 'covers/',default='covers/sample-image.jpg')
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True) 
    class Meta:
        ordering =  ['-created_at']

    def __str__(self) :
        return self.title






