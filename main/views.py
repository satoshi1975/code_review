from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .services import UserManagement
from django.contrib.auth import logout


from django.contrib.auth.models import User


def main_page(request):
    '''вывод главной страницы'''
    sign_up_form = RegistrationForm()
    log_in_form = LoginForm()
    return render(request, 'main_page.html',
                  context={'sign_up_form': sign_up_form, 'log_in_form': log_in_form})


def sign_up(request):
    '''обработка данных для регистрации'''
    res = UserManagement.register(request)
    return JsonResponse(res)


def log_in(request):
    '''обработка данных для входа'''
    if request.method == 'POST':
        response = UserManagement.log_in(request)
        return JsonResponse(response)


def log_out(request):
    """выход пользователя"""
    logout(request)
    return redirect('/')
