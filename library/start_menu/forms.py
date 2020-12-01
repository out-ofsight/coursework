from django.forms import ModelForm
from django import forms
from .models import Service, Author, Genre, Serie, Language, Book, Publishing_House



class ServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class AuthorAddForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorUpdateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class GenreUpdateForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class SerieUpdateForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = '__all__'


class LanguageUpdateForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'
    
class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'



class BookAddForm(forms.ModelForm):
    
    id_of_publish_house = forms.ModelChoiceField(queryset=Publishing_House.objects.all())
    id_of_series = forms.ModelChoiceField(queryset=Serie.objects.all())
    genre_book = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    author_book = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    service_book = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    language_book = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    year_of_wrote = forms.DateField(widget=DateInput)
    year_of_publishing = forms.DateField(widget=DateInput)
    class Meta:
        model = Book
        fields = '__all__'
        

class PublishingHouseUpdateForm(forms.ModelForm):
    class Meta:
        model = Publishing_House
        fields = '__all__'

