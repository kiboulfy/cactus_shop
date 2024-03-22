from django.contrib import admin
from django.urls import include, path
from users import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile')
]
    