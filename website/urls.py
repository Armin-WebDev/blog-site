
from django.urls import path
from .views import *

urlpatterns = [

    path('home/',home_view),
    path('about/',about_view),
    path('contact/',contact_view),
]
