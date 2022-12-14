from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','status')
    search_fields = ['title','content']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'description']

@admin.register(Category)
class CategoruAdmin(admin.ModelAdmin):
    pass