Django + redis + celery

Подписка на рассылку:

Выполнить в терминале команду запуска django:
python manage.py runserver

Выполнить команду запуска сервера redis:
redis-server #проверить соединение redis-cli > ping

Выполнить команду запуска celery:
celery --app send_email worker -l info


Выполнить рассылку:

Выполнить в терминале команду запуска django:
python manage.py runserver

Выполнить команду запуска сервера redis:
redis-server #проверить соединение redis-cli > ping

Выполнить команду запуска celery:
celery -A send_email beat -l info