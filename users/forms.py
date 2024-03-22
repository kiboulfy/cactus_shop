from django import forms 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AbstractUser
from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()
    '''username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True,
                                                            'class': 'users-tools__input-search',
                                                            'placeholder': 'Имя пользователя'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                          'class': 'users-tools__input-search',
                                          'placeholder': 'Пароль'}),
    )'''
    class Meta:
        model = User
        fields = ['username', 'password']
    