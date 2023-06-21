from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Account(models.Model):
    group = models.fields.CharField(max_length=100)
    name = models.fields.CharField(max_length=100)
    surname = models.fields.CharField(max_length=100)
    email = models.fields.EmailField()
    password = models.fields.CharField(max_length=1000)
    confirm_password = models.fields.CharField(max_length=1000)

    def __str__(self):
        return f'{self.name}'
