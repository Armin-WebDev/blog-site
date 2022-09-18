from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from website.models import Article,UserProfile
# Create your views here.

def home_view(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request,'website/index.html',context)

def about_view(request):
    return render(request,'website/page-about.html')

def contact_view(request):
    return render(request,'website/page-contact.html')

def category_view(request):
    return render(request,'website/category.html')

def single_article_view(request,pid): 
        articles = get_object_or_404(Article,pk = pid)
        context = {
        'article':articles,
        }
        return render(request,'website/single-standard.html', context)       