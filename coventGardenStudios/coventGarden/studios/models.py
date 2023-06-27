from django.contrib.auth.models import AbstractUser

from .fields import *

# Create your models here.
class CustomUser(AbstractUser):
    """
    Default
        username
        first_name
        last_name
        email
        password
    """

    """
    WIP
    phone
    my_groups
    my_bookings
    
    """

    test_field = MODELS_TEST

    def __str__(self):
        return self.username
