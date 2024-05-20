from django.shortcuts import render
from .models import Article, BlogsArticle
from django.views import View
# from django.views.generic import ListView


# Create your views here.

def home(request):
    articles = Article.objects.all()
    blog_articles = BlogsArticle.objects.all()
    return render(request, 'home/index.html', context={"articles": articles, "blog_articles": blog_articles})


# khod django list view dare albate baraye yeki hast
class ListView(View):
    articles = None
    blog_articles = None
    template_name = None

    def get(self, request):
        return render(request, self.template_name, {"articles": self.articles, "blog_articles": self.blog_articles})


class ArticleList(ListView):
    articles = Article.objects.all()
    blog_articles = BlogsArticle.objects.all()
    template_name = "home/blog.html"
