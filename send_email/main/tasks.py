from django.core.mail import send_mail
from send_email.celery import app

from .service import send
from .models import Contact


@app.task
def send_spam_email(user_email):
    send(user_email)


@app.task
def send_beat_email():
    for contact in Contact.objects.all():
        send_mail(
            'Вы подписались на рассылку',
            'Мы будем присылать вам информацию каждые 10 минут',
            'akashi_seidjuro547@mail.ru',
            [contact.email],
            fail_silently = False
        )