from celery import shared_task
from upload.models import CodeFile
from .services import is_code_valid
from code_check.settings import BASE_DIR

@shared_task
def check_code_files():
    '''задача проверки кода файла'''
    code_files = CodeFile.objects.filter(status__in=['new', 'updated'])
    for code_file in code_files:
        is_code_valid(code_file.file,code_file.id)
        code_file.status = 'tested'
        code_file.save()
