from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Service, Author, Book, Serie, Genre, Language, Publishing_House, User_Library, Profile
from .forms import ServiceUpdateForm, AuthorAddForm, AuthorUpdateForm, GenreUpdateForm, SerieUpdateForm, LanguageUpdateForm, PublishingHouseUpdateForm, BookAddForm, BookUpdateForm, FilterForm, SearchForm, SerieFilterForm
from django.views.generic import ListView, DetailView, TemplateView
from django.db import connection
import xml.etree.ElementTree as ET
import os
from django.template import Context
from django.views import View
from django.contrib.auth.models import User
from pathlib import Path
from django.core.files.storage import default_storage
from json import dumps 
from django.core.paginator import Paginator
from django.db.models import Count, Max
from django.utils import timezone
from io import BytesIO, StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template


def home(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'start_menu/start_menu.html', context)

def settings(request):
    return render(request, 'settings/settings.html')

def update_settings(request, pk):

    return render(request, 'settings/update_settings.html')

def update_book(request, pk):
    book = Book.objects.get(id=pk)
    form = BookUpdateForm(instance=book)

    if request.method == 'POST':
        form = BookUpdateForm(request.POST, instance=book)
        if form.is_valid():
            form.save()

    context = {'form':form, 'object':book}
    return render(request, 'settings/update_book_form.html', context)

def update_author(request, pk):
  
    author = Author.objects.get(id=pk)
    form = AuthorUpdateForm(instance=author)

    if request.method == 'POST':
        form = AuthorUpdateForm(request.POST, instance=author)
        if form.is_valid():
            form.save()

    context = {'form':form, 'object':author}
    return render(request, 'settings/update_author_form.html', context)

def update_service(request, pk):
    
    
    service = Service.objects.get(id=pk)
    form = ServiceUpdateForm(instance=service)

    if request.method == 'POST':
        form = ServiceUpdateForm(request.POST, instance=service)
        if form.is_valid():
            form.save()

    context = {'form':form, 'object':service}
    return render(request, 'settings/update_service.html', context)

def delete_service(request, pk):
    service = Service.objects.get(id=pk)
    if request.method == "POST":
        service.delete()
        return redirect('settings')
    context = {'object':service}
    return render(request, 'settings/delete_service.html', context)

def delete_genre(request, pk):
    genre = Genre.objects.get(id=pk)
    if request.method == "POST":
        genre.delete()
        return redirect('settings')
    context = {'object':genre}
    return render(request, 'settings/delete_genre.html', context)

def delete_language(request, pk):
    language = Language.objects.get(id=pk)
    if request.method == "POST":
        language.delete()
        return redirect('settings')
    context = {'object':language}
    return render(request, 'settings/delete_language.html', context)

def delete_author(request, pk):
    author = Author.objects.get(id=pk)
    if request.method == "POST":
        author.delete()
        return redirect('settings')
    context = {'object':author}
    return render(request, 'settings/delete_author.html', context)

def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == "POST":
        book.delete()
        return redirect('settings')
    context = {'object':book}
    return render(request, 'settings/delete_book.html', context)

#PB - publishing house
def delete_PB(request, pk):
    PB = Publishing_House.objects.get(id=pk)
    if request.method == "POST":
        PB.delete()
        return redirect('settings')
    context = {'object':PB}
    return render(request, 'settings/delete_PB.html', context)

def delete_serie(request, pk):
    serie = Serie.objects.get(id=pk)
    if request.method == "POST":
        serie.delete()
        return redirect('settings')
    context = {'object':serie}
    return render(request, 'settings/delete_serie.html', context)

def update_serie(request, pk):
  
    serie = Serie.objects.get(id=pk)
    form = SerieUpdateForm(instance=serie)

    if request.method == 'POST':
        form = SerieUpdateForm(request.POST, instance=service)
        if form.is_valid():
            form.save()

    context = {'form':form, 'object':serie}
    
    return render(request, 'settings/update_serie_form.html', context)

def update_publishing_house(request, pk):
  
    publishing_house = Publishing_House.objects.get(id=pk)
    form = PublishingHouseUpdateForm(instance=publishing_house)

    if request.method == 'POST':
        form = PublishingHouseUpdateForm(request.POST, instance=publishing_house)
        if form.is_valid():
            form.save()

    context = {'form':form, 'object':publishing_house}
    
    return render(request, 'settings/update_publishing_house_form.html', context)

def update_genre(request, pk):
  
    genre = Genre.objects.get(id=pk)
    form = GenreUpdateForm(instance=genre)

    if request.method == 'POST':
        form = GenreUpdateForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()

    context = {'form':form, 'object':genre}
    
    return render(request, 'settings/update_genre_form.html', context)

def update_language(request, pk):
  
    language = Language.objects.get(id=pk)
    form = LanguageUpdateForm(instance=language)

    if request.method == 'POST':
        form = LanguageUpdateForm(request.POST, instance=language)
        if form.is_valid():
            form.save()

    context = {'form':form, 'object':language}
    # поменять  html
    return render(request, 'settings/update_language_form.html', context)

class ServiceListView(ListView):
    model = Service
    context_object_name = 'servisies'
    ordering = ['-name']

class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    ordering = ['-id']

class GenreListView(ListView):
    model = Genre
    context_object_name = 'genres'
    ordering = ['-id']

class PublishingHouseListView(ListView):
    model = Publishing_House
    context_object_name = 'publishing_houses'
    ordering = ['-id']

class SerieListView(ListView):
    model = Serie
    context_object_name = 'series'
    ordering = ['-id']

class LanguageListView(ListView):
    model = Language
    context_object_name = 'languages'
    ordering = ['-id'] 

class ServiceDetailView(DetailView):
    model = Service

class AuthorDetailView(DetailView):

    model = Author

class GenreListView(ListView):
    model = Genre
    context_object_name = 'genres'
    ordering = ['-name']

class LanguageListView(ListView):

    model = Language
    context_object_name = 'languages'
    ordering = ['-name']

class SerieDetailView(DetailView):

    model = Serie
    
class GenreDetailView(DetailView):

    model = Genre

class LanguageDetailView(DetailView):

    model = Language

class PublishingHouseDetailView(DetailView):
    model = Publishing_House

class BookListView(ListView):
    model = Book
    context_object_name = 'books'

def add_settings_forms(request):

    book_form = BookAddForm(request.POST, request.FILES)
    context = {'book_form': book_form}
    if 'add_service' in request.POST:
        service_name = request.POST['service_name']
        opportunities = request.POST['opportunities']
        time_acvities = request.POST['time_acvities']
        service = Service(name=service_name, description=opportunities, time_to_use=time_acvities)
        if not Service.objects.filter(name=service_name).exists():
            service.save()
            
    if 'add_author' in request.POST:
        name = request.POST['name_author']
        information = request.POST['information']
        birth = request.POST['birth']
        death = request.POST['death']
        if death == '':
            author = Author(name=name,information_about=information,birth_date=birth)
            if not Author.objects.filter(name=name).exists():
             author.save()
        elif birth < death:
            author = Author(name=name,information_about=information,birth_date=birth,death_date=death)
            if not Author.objects.filter(name=name).exists():
             author.save()
        else:
            return redirect('start_search_menu')
    
    if 'add_genre' in request.POST:
        name = request.POST['name_genre']
        information = request.POST['information_of_genre']
        genre = Genre(name=name, description=information)
        if not Serie.objects.filter(name=name).exists():
            genre.save()
        
    if 'add_serie' in request.POST:
        name = request.POST['name_serie']
        information = request.POST['information_serie']
        is_ended = request.POST.get('is_ended', False)
        serie = Serie(name=name, is_ended=is_ended,description=information)
        if not Serie.objects.filter(name=name).exists():
            serie.save()
        
    if 'add_language' in request.POST:
        name = request.POST['name_language']
        language = Language(name=name)
        if not Language.objects.filter(name=name).exists():
            language.save()
    
    if 'add_publishing_house' in request.POST:
        name = request.POST['name_publishing_hose']
        location = request.POST['location']
        publishing_house = Publishing_House(name=name,location=location)
        if not Publishing_House.objects.filter(name=name).exists():
            publishing_house.save()
    
    if book_form.is_valid():
        if book_form.cleaned_data['year_of_wrote'] < book_form.cleaned_data['year_of_publishing'] and book_form.cleaned_data['page_count'] > 0:
            book_form.save()
            return redirect('settings')
        else:
            return redirect('start_search_menu')
    return render(request, 'settings/settings.html', context)

class BookDetailView(DetailView):
    context_object_name = 'book'
    model = Book   

def get_Book(request, pk):
    if request.user.is_authenticated:
        user_id = request.user.id
        user = request.user
        profile = Profile.objects.all().filter(user=user)
        service = Service.objects.filter(id__in=profile.values('service')).values('id')
        is_service_include = False
        book = Book.objects.all().get(id=pk)
        if Book.objects.filter(service_book__in=service).exists():
            is_service_include = True
    else:
        book = Book.objects.all().get(id=pk)
    text = []
    if Path(str(book.book_text_path)).suffix == '.fb2':
        tree = ET.parse(book.book_text_path)
        root = tree.getroot()
        tags = [elem.tag for elem in root.iter()]
        for i in tags:
            for description in root.iter(i):
                if description.tag.find('genre') == -1 and description.tag.find('first-name') == -1 and description.tag.find('second-name') == -1 and description.text is not None:
                    if description.text.strip():
                        text.append(description.text)
    elif Path(str(book.book_text_path)).suffix == '.txt':
        read_by_lines = False
        book_text = open(str(Path('media').parent.absolute()) + '/media/' + str(book.book_text_path))
        text = list(book_text)
        book_text.close()
    paginator = Paginator(text, 90)
    page_number = request.GET.get('page')
    text = paginator.get_page(page_number)
    book_id = pk
    if not request.user.is_authenticated:
        context = {
            'text': text,
            'book_id': book_id,
            'is_service_include':True
        }
    else:
        context = {
            'text': text,
            'book_id': book_id,
            'is_service_include':is_service_include
        }

    return render(request,'start_menu/book_detail.html', context)

def add_book_to_library(request):
    id_book = request.POST.get('book_id')
    book = Book.objects.get(id=id_book)
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    check_books = User_Library.objects.filter(id_user=user_id)
    temp = True
    for i in check_books.values('id_book_id'):
        if i['id_book_id'] == book.id:
            temp = False
            break
    if temp:
        new_book = User_Library(id_user=user,id_book=book)
        new_book.save()
        return redirect('start_search_menu')
    else:
        return redirect('user_library')
    return render(request, 'temp')

def bookList(request):
    genres = Genre.objects.all()
    books = Book.objects.all()
    filter_form = FilterForm(request.POST)
    search_form = SearchForm(request.POST)
    if request.method == 'POST':
        if filter_form.is_valid():
            genres = filter_form.cleaned_data['genres']
            authors = filter_form.cleaned_data['authors']
            series = filter_form.cleaned_data['series']
            PB = filter_form.cleaned_data['PB']
            PB_name = []
            genres_name = []
            authors_name = []
            series_name = []
            if len(PB) > 0:
                for i in PB:
                    PB_name.append(i)
                    PB = Publishing_House.objects.all().filter(name__in=PB_name).values('name')
                    books = Book.objects.filter(id_of_publish_house__name__in=PB_name)
            if len(genres) > 0:
                for i in genres:
                    genres_name.append(i)
                genres = Genre.objects.all().filter(name__in=genres_name).values('name')
                books = Book.objects.filter(genre_book__name__in=genres)
            if len(authors) > 0:
                for i in authors:
                    authors_name.append(i)
                authors = Author.objects.all().filter(name__in=authors_name).values('name')
                books = Book.objects.filter(author_book__name__in=authors)
            if len(series) > 0:
                for i in series:
                    series_name.append(i)
                series = Serie.objects.all().filter(name__in=series_name).values('name')
                books = Book.objects.filter(id_of_series__name__in=series)
            if 'decrease_sort' in request.POST:
                books = books.order_by('-name')
            if 'increase_sort' in request.POST:
                books = books.order_by('name')
        if search_form.is_valid():
            book_name = search_form.cleaned_data['book_name']
            books = Book.objects.filter(name__contains=book_name)
    context = {
        'books': books,
        'genres': genres,
        'filter_form': filter_form,
        'search_form': search_form,
    }
    return render(request, 'start_menu/books.html', context=context)

def user_library(request):
    if 'delete_button' in request.POST:
        User_Library.objects.filter(id_book=request.POST.get('delete_button')).delete()
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    books = User_Library.objects.filter(id_user=user).values('id_book')
    books = Book.objects.filter(id__in=books)
    context = {
        'books':books
    }
    return render(request, 'user_library.html', context)

def statictic_page(request):
    author = Author.objects.annotate(num_books=Count('book'))
    PH = Publishing_House.objects.annotate(num_books=Count('book'))
    service = Service.objects.annotate(num_service=Count('profile'))
    user_logged_in = User.objects.filter(last_login__startswith=timezone.now().date()).count()
    genre_author = Book.objects.values('author_book__name','genre_book__name').annotate(Count('id')).order_by('-id__count')
    user = User.objects.all()
    user_service = Service.objects.all()
    profile = Profile.objects.all()
    context = {
        'PH':PH,
        'author':author,
        'service': service,
        'user_logged_in':user_logged_in,
        'genre_author': genre_author,
        'user_service': user_service,
        'users':user,
        'profiles': profile
    }
    return render(request, 'statictic.html', context=context)

def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = context_dict
    html  = template.render(context)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def myview(request):
    time = timezone.now()
    users = User.objects.all()
    profile = Profile.objects.all() 
    service = Service.objects.all()
    books = Book.objects.all()
    library = User_Library.objects.all()
    context = {
        'time':time,
        'users': users,
        'profile':profile,
        'library': library,
        'books': books
        
    }
    return render_to_pdf(
            'report.html',
            {
                'pagesize':'A4',
                'context': context
            }
        )

def user_report(request):
    time = timezone.now()
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    books = User_Library.objects.filter(id_user=user).values('id_book')
    books = Book.objects.filter(id__in=books)
    context = {
        'time': time,
        'user':user,
        'books':books
    }
    return render_to_pdf(
            'user_report.html',
            {
                'pagesize':'A4',
                'context': context
            }
        )

def delete_user_book(request, pk):
    if request.method == "POST":
        book = User_Library.objects.get(id=pk)
        book.delete()
        return redirect('user_library')
    book = User_Library.objects.get(id_user=request.user.id,id_book=pk)
    context = {'object':book}
    return render(request, 'delete_book_fr_lb.html', context)

def series_page(request):
    filter_form = SerieFilterForm()
    series = Serie.objects.all()
    if request.method == 'POST':
        if 'decrease_sort' in request.POST:
            series = series.order_by('-name','-is_ended')
            context = {
            'series': series,
            'filter_form': filter_form
        }
            return render(request, 'start_menu/series.html', context)
        elif 'increase_sort' in request.POST:
            series = series.order_by('name','is_ended')
            context = {
                'series': series,
                'filter_form': filter_form
                }
            return render(request, 'start_menu/series.html', context)
        if request.POST.get('is_ended_serie', False):
            series = series.filter(is_ended=True)
        elif request.POST.get('is_ended_serie', False) is False:
            series = series.filter(is_ended=False)
    context = {
        'series': series,
        'filter_form': filter_form
        }
    return render(request, 'start_menu/series.html', context)

def serie_page(request, pk):

    books = Book.objects.all().filter(id_of_series=pk)
    context = {
        'books':books
    }
    return render(request, 'start_menu/serie.html', context)

def genres_page(request):
    genres = Genre.objects.all()
    if request.method == 'POST':
        if 'decrease_sort' in request.POST:
            genres = genres.order_by('-name')
        elif 'increase_sort' in request.POST:
            genres = genres.order_by('name')
    context = {
        'genres':genres
    }
    return render(request, 'genres.html', context)

def genre_page(request, pk):

    books = Book.objects.filter(genre_book__id=pk)
    genre = Genre.objects.get(id=pk)
    context = {
        'books': books,
        'genre': genre
    }
    return render(request, 'genre.html', context)

def author(request):
    authors = Author.objects.all()
    if request.method == 'POST':
        if 'decrease_sort' in request.POST:
            authors = authors.order_by('-name')
        elif 'increase_sort' in request.POST:
            authors = authors.order_by('name')
    context = {
    'authors': authors
    }
    return render(request, 'authors.html', context)

def author_book(request, pk):
    books = Book.objects.filter(author_book__id=pk)
    genre = Author.objects.get(id=pk)
    context = {
        'books': books,
        'author': author
    }
    return render(request, 'author.html', context)