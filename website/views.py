from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    return HttpResponse('Welcome to the Home Page')

def about_view(request):
    return HttpResponse('Welcome to the About Page')

def contact_view(request):
    return HttpResponse('Welcome to the Contact Page')