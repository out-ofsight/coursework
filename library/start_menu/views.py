from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Service, Author, Book, Serie, Genre, Language, Publishing_House
from .forms import ServiceUpdateForm, AuthorAddForm, AuthorUpdateForm, GenreUpdateForm, SerieUpdateForm, LanguageUpdateForm, PublishingHouseUpdateForm, BookAddForm
from django.views.generic import ListView, DetailView, TemplateView
from django.db import connection
from lxml import objectify
# Create your views here.

def home(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'start_menu/start_menu.html', context)

def settings(request):
    return render(request, 'settings/settings.html')

'''def add_settings(request):
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
        author = Author(name=name,information_about=information,birth_date=birth,death_date=death)
        if not Author.objects.filter(name=name).exists():
            author.save()
    
    if 'add_genre' in request.POST:
        name = request.POST['name_genre']
        information = request.POST['information_of_genre']
        genre = Genre(name=name, description=information)
        if not Serie.objects.filter(name=name).exists():
            genre.save()
        
    if 'add_serie' in request.POST:
        name = request.POST['name_serie']
        information = request.POST['information_serie']
        is_ended = request.POST['is_ended']
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
    

    return render(request, 'settings/settings.html')
 '''
def update_settings(request, pk):

    return render(request, 'settings/update_settings.html')

def update_author(request, pk):
  
    author = Author.objects.get(id=pk)
    form = AuthorUpdateForm(instance=author)

    if request.method == 'POST':
        form = AuthorUpdateForm(request.POST, instance=service)
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
        return redirect('update_settings')
    context = {'object':service}
    return render(request, 'settings/delete_service.html', context)

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
    def get_author(self):
        author_name = Book.objects.get(name=self.name).author_book.all()

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
        author = Author(name=name,information_about=information,birth_date=birth,death_date=death)
        if not Author.objects.filter(name=name).exists():
            author.save()
    
    if 'add_genre' in request.POST:
        name = request.POST['name_genre']
        information = request.POST['information_of_genre']
        genre = Genre(name=name, description=information)
        if not Serie.objects.filter(name=name).exists():
            genre.save()
        
    if 'add_serie' in request.POST:
        name = request.POST['name_serie']
        information = request.POST['information_serie']
        is_ended = request.POST['is_ended']
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
        book_form.save()
        return redirect('settings')
    return render(request, 'settings/settings.html', context)

class BookDetailView(DetailView):
    context_object_name = 'book'
    model = Book
    

def get_Book(request, pk):
    book = Book.objects.get(id=pk)
    xml_book = objectify.parse(book.book_text_path)
    root = xml_book.getroot()
    temp = [child.text for child in root.Book.getchildren()]
    context = {
        'book':temp,
    }
    return render(request,'start_menu/book_detail.html', context)

