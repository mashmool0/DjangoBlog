from django.urls import path
from . import views

name_app = 'home_app'
urlpatterns = [
    path('', views.home, name='home'),
]
