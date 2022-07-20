from django.core.mail import send_mail

def send(user_email):
    send_mail(
        'Вы подписались на рассылку',
        'Мы будем отправлять вам интересные предложения и акции',
        'akashi_seidjuro547@mail.ru',
        [user_email],
        fail_silently=False,
    )