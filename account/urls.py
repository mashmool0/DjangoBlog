from django.urls import path
from . import views

app_name = 'contactus_app'
urlpatterns = [
    path('contactus', views.contact, name='contactus'),
    path('login', views.user_login, name="login"),
    path('register', views.user_register, name="register"),
    path('', views.user_logout, name='logout'),
    path('edit', views.user_edit, name='edti'),
]
