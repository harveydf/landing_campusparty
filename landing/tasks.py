import json

from celery import task
from .models import UserRegistered, Mail

@task(max_retries=3)
def register_user(name, email):
    try:
        user_registered = UserRegistered.objects.create(name=name, email=email)
    except Exception, e:
        register_user.retry(exc=e, countdown=60)

    return user_registered


@task()
def save_welcome_mail(user_registered):
    Mail.objects.create(
        subject='Bienvenido a Campus Party v6',
        to=user_registered.email,
        from_email='campus@party.co',
        template='welcome.html',
        data=json.dumps(dict(name=user_registered.name, email=user_registered.email, token=user_registered.token))
    )
