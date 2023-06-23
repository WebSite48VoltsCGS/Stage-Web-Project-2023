from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here

class Group(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255)
    # phone = FIELD_PHONE
    members = models.CharField(max_length=255)
    musical_style = models.CharField(max_length=255)
    diet = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    participants = models.CharField(max_length=255)
    biography = models.CharField(max_length=255)
