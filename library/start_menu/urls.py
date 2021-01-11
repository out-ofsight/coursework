from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from users import views as user_views
from django.contrib.auth import views as auth_views
from .views import ServiceListView, ServiceDetailView, AuthorListView, AuthorDetailView, GenreDetailView, SerieDetailView, LanguageDetailView, GenreListView, LanguageListView, SerieListView, PublishingHouseDetailView, PublishingHouseListView, BookListView


urlpatterns = [
    path('', views.home, name='start_search_menu'),
    path('series', views.series_page, name='series_page'),
    path('serie/<int:pk>', views.serie_page, name='serie_page'),
    path('register/', user_views.registerPage, name='regestration_menu'),
    path('genres/', views.genres_page, name='genre_page'),
    path('genre/<int:pk>', views.genre_page, name='genre_book_page'),
    path('login/', user_views.login, name ='login'),
    #path('login/', user_views.LoginView1.as_view(), name ='login'),
    path('logout/', user_views.logout_user, name ='logout'),
    path('authors/', views.author, name='author_page'),
    path('author/<int:pk>', views.author_book, name='author_book'),
    path('profile/', user_views.profile, name='profile'),
    path('user_report/', views.user_report, name='user_report'),
    path('user_library/', views.user_library, name='user_library'),
    path('to_pdf/', views.myview, name='to_pdf_report'),
    path('delete_user_book/<int:pk>', views.delete_user_book, name='delete_user_book'),
   # path('settings/', views.add_settings_forms, name='settings'),
    path('books', views.bookList, name='books'),
    #path('book/<int:pk>/', views.BookDetailView.as_view(template_name='start_menu/book_detail.html'), name='book_detail'),
    path('book/<int:pk>/', views.get_Book, name='book_detail'),
    path('add_settings/', views.add_settings_forms, name='settings'),
    path('update_settings/', ServiceListView.as_view(template_name='settings/update_settings.html'), name='update_settings'),
    path('update_settings/<int:pk>/', ServiceDetailView.as_view(template_name='settings/detail_service.html'), name='detail_view'),
    path('update_author/', AuthorListView.as_view(template_name='settings/update_author.html'), name='author_update'),
    path('update_genre/', GenreListView.as_view(template_name='settings/update_genre.html'), name='genre_update'),
    path('update_serie/', SerieListView.as_view(template_name='settings/update_serie.html'), name='serie_update'),
    path('statictic_page/', views.statictic_page, name='statictic_page'),
    path('update_publishing_house/<int:pk>/', PublishingHouseDetailView.as_view(template_name='settings/detail_publishing_house.html'), name='detail_publishing_house'),
    path('update_publishing_house/', PublishingHouseListView.as_view(template_name='settings/update_publishing_house.html'), name='publishing_house_update'),
    path('update_language/', LanguageListView.as_view(template_name='settings/update_language.html'), name='language_update'),
    path('update_author/<int:pk>/', AuthorDetailView.as_view(template_name='settings/detail_author.html'), name='detail_author'),
    path('update_genre/<int:pk>/', GenreDetailView.as_view(template_name='settings/detail_genre.html'), name='detail_genre'),
    path('update_serie/<int:pk>/', SerieDetailView.as_view(template_name='settings/detail_serie.html'), name='detail_serie'),
    path('update_language/<int:pk>/', LanguageDetailView.as_view(template_name='settings/detail_language.html'), name='detail_language'),
    path('update_service/<int:pk>/', views.update_service, name='update_service'),
    path('update_author_form/<int:pk>/', views.update_author, name='update_author_form'),
    path('update_genre_form/<int:pk>/', views.update_genre, name='update_genre_form'),
    path('update_serie_form/<int:pk>/', views.update_serie, name='update_serie_form'),
    path('update_language_form/<int:pk>/', views.update_language, name='update_language_form'),
    path('update_publishing_house_form/<int:pk>/', views.update_publishing_house, name='update_publishing_house_form'),
    path('delete_service/<int:pk>/', views.delete_service, name="delete_service"),
    path('delete_book/<int:pk>/', views.delete_book, name="delete_book"),
    path('delete_PB/<int:pk>/', views.delete_PB, name="delete_PB"),
    path('delete_language/<int:pk>/', views.delete_language, name="delete_language"),
    path('delete_genre/<int:pk>/', views.delete_genre, name="delete_genre"),
    path('delete_author/<int:pk>/', views.delete_author, name="delete_author"),
    path('delete_serie/<int:pk>/', views.delete_serie, name="delete_serie"),
    path('update_book/', views.BookListView.as_view(template_name='settings/update_book.html'), name='book_update'),
    path('update_book/<int:pk>/', views.BookDetailView.as_view(template_name='settings/detail_book.html'), name='detail_book'),
    path('update_book_form/<int:pk>/', views.update_book, name='update_book_form'),
    path('add_book_to_library', views.add_book_to_library ,name='add_book_to_library'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
