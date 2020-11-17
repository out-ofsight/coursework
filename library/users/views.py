from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def registerPage(request):  
    form = CreationForm()
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Аккаунт создан ' + username)
            return redirect('start_search_menu')
    else:
        form = CreationForm()
    context = {'form': form}
    return render(request, 'regestration_menu/regestration_menu.html', context)

def loginPage(request):
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

def logoutUser(request):
    logout(request)
    return redirect('start_search_menu')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Вы обновили данные!')
            return redirect('start_search_menu')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile_page/profile.html', context)

