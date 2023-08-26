'''конфигурация celery'''
import os
from celery import Celery
from django.conf import settings
from datetime import timedelta
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'code_check.settings')

app = Celery('your_project_name')

app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()

# задача по переодической проверке файлов
app.conf.beat_schedule = {
    'check-code-every-minute': {
        'task': 'code_review.tasks.check_code_files',
        'schedule': timedelta(minutes=1),
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
