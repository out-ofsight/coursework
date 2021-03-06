from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from start_menu.models import Book, Profile, Service
from django.contrib.auth.models import User
import datetime
from django.views.generic import View

def registerPage(request):  
    form = CreationForm()
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Аккаунт создан ' + username)
            template = render_to_string('email/template.html', {'name': username})
            email = EmailMessage(
                'Добро пожаловать',
                template,
                settings.EMAIL_HOST_USER,
                [form.cleaned_data.get('email')]
            )
            email.fail_silently = False
            email.send()
            return redirect('start_search_menu')
    else:
        form = CreationForm()
    context = {'form': form}
    return render(request, 'regestration_menu/regestration_menu.html', context)


class LoginView1(View):
    def post(self, request):
        username = request.post.get('username')
        password = request.post.get('password')
        user = authenticate(request, username=username, password=password)
        tuple_data = get_user_and_profile(username)
        current_user, current_profile = tuple_data
        user_service = Service.objects.get(id=current_profile.service)
        if check_date(user_service.time_to_use, current_profile.server_connection_date):
            delete_service(current_profile)
        if user is not None:

            login(request, user)
            return redirect('start_search_menu')
        else:
            messages.info(request, 'Пароль или имя пользывателя неправильные')
    def get(self, request):
        return render(request, 'login_menu/login.html', context)
'''
def login(request):
    if request.method == 'POST':
        username = request.post.get('username')
        password = request.post.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)
            return redirect('start_search_menu')
        else:
            messages.info(request, 'Пароль или имя пользывателя неправильные')
    context = {}
    return render(request, 'login_menu/login.html', context)
'''
def logout_user(request):
    current_user = request.user
    current_profile = None
    try:
        current_profile = Profile.objects.filter(user=current_user, service__isnull=False).get(user=current_user)
    except BaseException:
        current_profile = None
    if current_profile is not None:
        current_service_id = current_profile.service.id
        user_service = Service.objects.get(id=current_service_id)
        if check_date(user_service.time_to_use, current_profile.server_connection_date):
            delete_service(current_profile)
    logout(request)
    return redirect('start_search_menu')

@login_required
def profile(request):
    user = request.user
    user_profile = Profile.objects.all().get(user_id__pk=user.id)
    service_time = None
    try:
        service_time = datetime.timedelta(days=user_profile.service.time_to_use)
    except BaseException:
        service_time = None
    
    if service_time is not None:
        service_time += datetime.date.today()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            instance = p_form.save(commit=False)
            instance.server_connection_date = datetime.date.today()
            instance.save()
            if p_form.cleaned_data['service'] is None:
                service = p_form.save(commit=False)
                service.server_connection_date = None
                service.save()
            p_form.save()
            if p_form.cleaned_data['service']:
                user_service = p_form.cleaned_data['service']
                today = datetime.date.today()
                user_profile.server_connection_date = today
                user_profile.save()
                try:
                    if p_form.cleaned_data['service'] != user_profile.service:
                        books = Book.objects.filter(service_book__name=user_service).values('name')
                        books_name = ''            
                        for i in books:
                            books_name+=i['name'] + ', '
                        template = render_to_string('email/new_service.html', {'name': user.username, 'books': books_name})
                        email = EmailMessage(
                        'Сервис обновлён',
                        template,
                        settings.EMAIL_HOST_USER,
                        [user.email]
                    )
                        email.fail_silently = False 
                        email.send()
                except BaseException:
                    books = Book.objects.filter(service_book__name=user_service).values('name')
                    books_name = ''            
                    for i in books:
                        books_name+=i['name'] + ', '
                    template = render_to_string('email/new_service.html', {'name': user.username, 'books': books_name})
                    email = EmailMessage(
                    'Сервис добавлен',
                    template,
                    settings.EMAIL_HOST_USER,
                    [user.email]
                    )
                    email.fail_silently = False 
                    email.send()

            p_form.save()
            return redirect('start_search_menu')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'service_time': service_time

    }
    return render(request, 'profile_page/profile.html', context)




def check_date(time_action, user_connection_date):
    date_list = list(map(int, str(user_connection_date).split('-')))
    user_connection_date = datetime.date(year=date_list[0], month=date_list[1], day=date_list[2])
    current_date = datetime.date.today()
    if datetime.timedelta(days=time_action) + user_connection_date < current_date:
        return True
    else:
        return False

def get_user_and_profile(username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    return (user, profile)

def delete_service(profile):
    profile.service = None
    profile.server_connection_date = None
    profile.save()

