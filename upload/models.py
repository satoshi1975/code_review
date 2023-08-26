from django.db import models
from main.models import CustomUser


def user_directory_path(instance, filename):
    '''генерация пути для файлов пользователя'''
    return f'user_code/{instance.user.id}/{filename}'


class CodeFile(models.Model):
    '''модель файла .py'''
    STATUS_CHOICES = [
        ('new', 'New'),
        ('updated', 'Updated'),
        ('tested', 'Tested'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='new'
    )

    def get_file_path(self):
        return f'user_code/{self.user.id}/{self.file.name}'
