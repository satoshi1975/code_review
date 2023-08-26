from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    '''форма регистрации пользователя'''

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['email'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    '''форма верификации данных для входа'''

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        del self.fields['username']
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}))
