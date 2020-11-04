from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request, 'start_menu/start_menu.html')

#def regestration(request):
 #   return render(request, 'regestration_menu/regestration_menu.html')