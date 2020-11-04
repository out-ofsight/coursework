from users import views as user_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('regester/', user_views.register, name='regester'),
    path('', include('start_menu.urls')),

]
