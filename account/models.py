from django.db import models


# Create your models here.

class UserTeacher(models.Model):
    fullname = models.CharField(max_length=30, verbose_name="نام ونام خانوادگی")
    email = models.EmailField(blank=True, null=True, verbose_name='آدرس ایمیل')
    phone_number = models.IntegerField(verbose_name="شماره تلفن")
    profile = models.ImageField(upload_to='media', verbose_name="عکس پروفایل", default="static/profile/22_Profile.jpg")

    class Meta:
        verbose_name = "حساب کاربری استاد"
        verbose_name_plural = "حساب های کاربری اساتید"


class UserStudent(models.Model):
    fullname = models.CharField(max_length=30, verbose_name="نام ونام خانوادگی")
    email = models.EmailField(verbose_name='آدرس ایمیل')
    phone_number = models.IntegerField(verbose_name="شماره تلفن")
    codeID = models.IntegerField(primary_key=True, verbose_name='کد ملی')
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    # complete details
    date_birthday = models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')
    profile = models.ImageField(upload_to='media', verbose_name="عکس پروفایل", default="static/profile/22_Profile.jpg")
    father_name = models.CharField(max_length=30, blank=True, null=True)
    mother_name = models.CharField(max_length=30, blank=True, null=True)
    parent_phone = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "حساب کاربری دانش آموز"
        verbose_name_plural = "حساب های کاربری دانش آموزان"
