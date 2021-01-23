from django.contrib import admin
from django.urls import path

from registerProfile import views

app_name = "registerProfile"
urlpatterns = [
    path('', views.index, name='index')
]