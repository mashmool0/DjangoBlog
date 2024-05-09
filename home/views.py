from django.shortcuts import render
from .models import Article, BlogsArticle


# Create your views here.

def home(request):
    articles = Article.objects.all()
    blog_articles = BlogsArticle.objects.all()
    return render(request, 'home/index.html', context={"articles": articles, "blog_articles": blog_articles})
