from django.db import models
from upload.models import CodeFile


class CheckLog(models.Model):
    '''модель логов файла'''
    file = models.ForeignKey(
        CodeFile, on_delete=models.CASCADE) 
    timestamp = models.DateTimeField(auto_now_add=True)
    passed = models.BooleanField(default=False, null=True)
    details = models.TextField(default=None, null=True)
    mailed = models.BooleanField(default=None, null=True, blank=True)

    def __str__(self):
        return f"CheckLog for {self.file.name} by {self.user.username}"
