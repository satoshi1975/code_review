import os
from .forms import LoginForm, RegistrationForm
from code_check import settings
from .models import CustomUser
from django.contrib.auth import login,authenticate

class UserManagement:
    '''функционал управления аккаунтом'''
    
    @staticmethod
    def register(request):
        '''регистрация пользователя'''
        form=RegistrationForm(request.POST)
        email = request.POST.get('email')

        if form.is_valid():
            if CustomUser.objects.filter(email=email).exists() == False:
                user = form.save()
                login(request,user)
                UserManagement.user_file_folder(user.id) #создание папки для файлов пользователя
                return {'success': True}
            else:
                return {'success': False,'error_message':'The email already exists'}
            
        else:
            error_message = form.error_messages[next(iter(form.error_messages))]
            return {'success': False, 'error_message': error_message }
    
    @staticmethod
    def user_file_folder(user_id):
        '''создание папки для пользователя'''
        folder_path = os.path.join(settings.BASE_DIR,'user_code',f'{user_id}')
        os.makedirs(folder_path, exist_ok=True)

    @staticmethod
    def log_in(request):
        '''авторизация'''
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return {'success':True}
            else:
                return {'success':False,'error_message':'Incorrect email or password'}
        else:
            error_message = form.error_messages[next(iter(form.error_messages))]
            return {'success':False, 'error_message':error_message}
    
    