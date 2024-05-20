from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='نویسنده')
    title = models.CharField(max_length=30,verbose_name='عنوان')
    description = models.CharField(max_length=100,verbose_name='توضیحات')
    date = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ انتشار')
    image = models.ImageField(null=True, upload_to='media',verbose_name='عکس')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = 'مقالات'


class Messages(models.Model):
    title = models.CharField(max_length=100,verbose_name='عنوان')
    text = models.TextField(verbose_name='متن')
    email = models.EmailField(verbose_name='آدرس ایمیل')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = 'پیام ها'


class BlogsArticle(models.Model):
    title = models.CharField(max_length=40,verbose_name='عنوان')
    description_small = models.CharField(max_length=100,verbose_name='توضیحات کوتاه')
    description_complete = models.TextField(verbose_name='توضیحات کامل')
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='نویسنده')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "بلاگ"
        verbose_name_plural = 'بلاگ ها'
