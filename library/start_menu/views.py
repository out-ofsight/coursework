from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Service, Author
from .forms import ServiceUpdateForm, AuthorAddForm
from django.views.generic import ListView, DetailView, TemplateView
# Create your views here.

def home(request):
    return render(request, 'start_menu/start_menu.html')

def settings(request):
    return render(request, 'settings/settings.html')

def add_settings(request):
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
    return render(request, 'settings/settings.html')
 
def update_settings(request, pk):

    return render(request, 'settings/update_settings.html')

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


class ServiceListView(ListView):
    model = Service
    context_object_name = 'servisies'
    ordering = ['-name']

class ServiceDetailView(DetailView):
    model = Service
