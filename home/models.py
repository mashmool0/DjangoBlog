from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, upload_to='media')

    def __str__(self):
        return self.title


class Messages(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogsArticle(models.Model):
    title = models.CharField(max_length=40)
    description_small = models.CharField(max_length=100)
    description_complete = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
