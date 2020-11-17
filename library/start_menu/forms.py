from django.forms import ModelForm
from django import forms
from .models import Service, Author



class ServiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

class AuthorAddForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'