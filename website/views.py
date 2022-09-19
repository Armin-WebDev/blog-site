from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from website.models import Article,UserProfile
# Create your views here.

def home_view(request):
    categories=[]
    artcile_for_category=[]
    articles = Article.objects.all()[:9]
    promote_articles = Article.objects.filter(status = True)[:3]
    for article in articles:
        if article.category not in categories:
            categories.append(article.category)
            artcile_for_category.append(article)

    context = {
        'articles':articles,
        'promoted':promote_articles,
        'categories':artcile_for_category
    }
    return render(request,'website/index.html',context)

def about_view(request):
    return render(request,'website/page-about.html')

def contact_view(request):
    return render(request,'website/page-contact.html')

def category_view(request):
    categories=[]
    artcile_for_category=[]
    articles = Article.objects.all()[:9]
    promote_articles = Article.objects.filter(status = True)[:3]
    for article in articles:
        if article.category not in categories:
            categories.append(article.category)
            artcile_for_category.append(article)

    context = {
        'articles':articles,
        'promoted':promote_articles,
        'categories':artcile_for_category
    }
    return render(request,'website/category.html',context)

def single_article_view(request,pid):
        articles = get_object_or_404(Article,pk = pid)
        context = {
        'article':articles,
        }
        return render(request,'website/single-standard.html', context)       