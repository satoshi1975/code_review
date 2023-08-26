import subprocess
import os
from upload.models import CodeFile
from code_check.settings import BASE_DIR
from .models import CheckLog
from email_logs.tasks import send_email


def is_code_valid(file_path, file_id):
    '''проверка кода из файла на соответсвие нормам'''
    file_obj = CodeFile.objects.get(id=file_id)
    file_log, create = CheckLog.objects.get_or_create(file=file_obj)
    user_email = file_obj.user.email
    full_path = os.path.join(BASE_DIR, f'{file_path}')
    try:
        output = subprocess.check_output(
            ['flake8', full_path], stderr=subprocess.STDOUT, text=True)
        if not output.strip():
            send_email.delay('Code Check Result', 'Your code is currect.',  # задача оп отправке емейла
                             [user_email], file_log.id)
            file_log.passed = True
            file_log.details = 'Correct'
            file_log.save()
            return True
        else:
            send_email.delay('Code Check Result', 'Validation error',
                             [user_email], file_log.id)  # задача оп отправке емейла
            file_log.passed = False
            file_log.details = 'Validation error'
            file_log.save()
            return False
    except subprocess.CalledProcessError as e:
        send_email.delay('Code Check Result', f'Validation error:{e.output}',
                         [user_email], file_log.id)  # задача оп отправке емейла
        file_log.passed = False
        file_log.details = f'{e.output}'
        file_log.save()
        return False
