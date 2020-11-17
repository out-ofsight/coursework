from django.contrib import admin
from django.urls import path
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from .views import ServiceListView, ServiceDetailView


urlpatterns = [
    path('', views.home, name='start_search_menu'),
    path('register/', user_views.registerPage, name='regestration_menu'),
    path('login/', auth_views.LoginView.as_view(template_name='login_menu/login.html', redirect_field_name='start_search_menu'), name ='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='start_menu/start_menu.html'), name ='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('add_settings/', views.add_settings, name='add_settings'),
    path('update_settings/', ServiceListView.as_view(template_name='settings/update_settings.html'), name='update_settings'),
    path('update_settings/<int:pk>/', ServiceDetailView.as_view(template_name='settings/detail_service.html'), name='detail_view'),
    path('update_service/<int:pk>/', views.update_service, name='update_service'),
    path('delete_service/<int:pk>/', views.delete_service, name="delete_service"),
]
