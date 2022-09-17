from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    return render(request,'website/index.html')

def about_view(request):
    return render(request,'website/page-about.html')

def contact_view(request):
    return render(request,'website/page-contact.html')

def category_view(request):
    return render(request,'website/category.html')

def test_view(request):
    return render(request,'website/single-standard.html')     