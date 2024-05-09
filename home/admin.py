from django.contrib import admin
from .models import Article, Messages, BlogsArticle

# Register your models here.
admin.site.register(Article)
admin.site.register(Messages)
admin.site.register(BlogsArticle)

