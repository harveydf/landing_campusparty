from celery import task

from .models import UserRegistered

@task(max_retries=3)
def register_user(name, email):
    try:
        UserRegistered.objects.create(name=name, email=email)
    except Exception, e:
        register_user.retry(exc=e, countdown=60)
