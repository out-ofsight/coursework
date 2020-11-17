from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



#



class CreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        labels = {
            'username': 'Имя на сайте',
            'email': 'Електронная почта',
            'password1': 'Пароль',
            'password2': 'Подтвердите пароль',
        }
