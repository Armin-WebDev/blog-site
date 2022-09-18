
from unicodedata import category
from django.urls import path
from .views import *

urlpatterns = [

    path('',home_view , name='home'),
    path('about/',about_view, name='about'),
    path('contact/',contact_view, name='contact'),
    path('category/' , category_view , name='category'),
    path('post-<int:pid>',single_article_view, name='single-article')
]
