'''отправка писем с логами'''
from django.core.mail import send_mail
from celery import shared_task
from .services import new_email


@shared_task
def send_email(subject, message, recipient_list, log_id):
    '''задача по отправке письма с логами'''
    new_email(subject, message, recipient_list, log_id)
