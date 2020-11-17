from users import views as user_views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('regester/', user_views.registerPage, name='regester'),
    path('', include('start_menu.urls')),
    path('login', auth_views.LoginView.as_view(template_name='login_menu/login.html'), name ='login'),
    path('logout', auth_views.LogoutView.as_view(), name ='logout'),
    path('profile', user_views.profile, name='profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)