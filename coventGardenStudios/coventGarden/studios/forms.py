from django.contrib.auth.forms import (UserCreationForm, UserChangeForm, PasswordResetForm, SetPasswordForm)
from .models import CustomUser
from .fields import *

# Register your forms here
"""
Tutorial
"""
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")

"""
Main
"""
class SignInForm(forms.Form):
    username = FORM_USERNAME
    password = FORM_PASSWORD

class SignUpForm(forms.Form):
    username = FORM_USERNAME
    email = FORM_EMAIL
    last_name = FORM_LAST_NAME
    first_name = FORM_FIRST_NAME
    password = FORM_PASSWORD
    confirm_password = FORM_CONFIRM

class UserPasswordResetForm(PasswordResetForm):
    # Replaced PasswordResetForm fields with custom fields (See docs)
    email = FORM_EMAIL

class UserPasswordSetForm(SetPasswordForm):
    # Replaced SetPasswordForm fields with custom fields (See docs)
    new_password1 = FORM_PASSWORD
    new_password2 = FORM_CONFIRM

class TestForm(forms.Form):
    test = FORM_GROUP_NAME
