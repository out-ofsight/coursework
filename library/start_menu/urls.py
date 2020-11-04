from django.contrib import admin
from django.urls import path
from . import views
from users import views as user_views

urlpatterns = [
    path('', views.home, name='start_search_menu'),
    path('register', user_views.register, name='regestration_menu'),
    
]
