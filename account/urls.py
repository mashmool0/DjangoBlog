from django.urls import path
from . import  views

app_name = 'contactus_app'
urlpatterns = [
    path('',views.contact,name='contactus')
]