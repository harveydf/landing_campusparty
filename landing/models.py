from django.db import models

class UserRegistered(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
