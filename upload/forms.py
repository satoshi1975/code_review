from django import forms

class UploadFileForm(forms.Form):
    '''форма для файла .py'''
    ALLOWED_EXTENSION = 'py'
    file = forms.FileField()
