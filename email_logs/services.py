'''емейл рассылка логов'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from code_review.models import CheckLog


def new_email(subject, message, recipient_list, log_id):
    '''отправка логов на почту пользователя'''
    log = CheckLog.objects.get(id=log_id)

    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'my_mail@gmail.com'
    sender_password = 'cxomvivxuxrztqcn'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(recipient_list)
    msg['Subject'] = Header(subject, 'utf-8')

    body = MIMEText(message, 'plain', 'utf-8')
    msg.attach(body)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_list, msg.as_string())
        server.quit()
        log.mailed = True
        log.save()
    except Exception as e:
        log.mailed = False
        log.save()
