from django.contrib import admin
from .models import UserTeacher, UserStudent

# Register your models here.
# admin.site.site_header = "مدیریت مدرسه"
admin.site.register(UserTeacher)
admin.site.register(UserStudent)
