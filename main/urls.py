from django.contrib import admin
from django.urls import path, include
from main import views
from users import urls

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]