from django import forms
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import RegionalPhoneNumberWidget
from studios.models import Group

# Fields
def field_name(label, required=True):
    return forms.CharField(max_length=150, label=label, required=required,
                           widget=forms.TextInput(attrs={"class": "form-control"}))

def field_email(label, required=True):
    return forms.EmailField(max_length=255, label=label, required=required,
                            widget=forms.TextInput(attrs={"class": "form-control"}))

def field_password(label, required=True):
    return forms.CharField(max_length=255, label=label, required=required,
                           widget=forms.PasswordInput(attrs={"class": "form-control"}))

def field_text(label, required=True):
    return forms.CharField(max_length=5000, label=label, required=required,
                           widget=forms.Textarea(attrs={"class": "form-control"}))

def field_phone(label, required=True):
    return PhoneNumberField(region="FR", label=label, required=required,
                            widget=RegionalPhoneNumberWidget(attrs={"class": "form-control"}))

FIELD_USERNAME = field_name("Nom d'utilisateur")
FIELD_LAST_NAME = field_name("Nom")
FIELD_FIRST_NAME = field_name("Prénom")
FIELD_GROUP_NAME = field_name("Nom de groupe")
FIELD_MEMBERS = field_name("Membre(s)")
FIELD_MUSICAL_STYLE = field_name("Style musical")
FIELD_DIET = field_name("Régime alimentaire")
FIELD_FACEBOOK = field_name("Facebook", required=False)
FIELD_INSTAGRAM = field_name("Instagram", required=False)
FIELD_TWITTER = field_name("Twitter", required=False)
FIELD_PARTICIPANTS = field_name("Participant(s) supplémentaire(s)", required=False)

FIELD_EMAIL = field_email("Adresse e-mail")

FIELD_PASSWORD = field_password("Mot de passe")
FIELD_CONFIRM = field_password("Confirmer le mot de passe")

FIELD_BIOGRAPHY = field_text("Biographie")

FIELD_PHONE = field_phone("Numéro de téléphone")


# Register your forms here
class SignInForm(forms.Form):
    username = FIELD_USERNAME
    password = FIELD_PASSWORD

class SignUpForm(forms.Form):
    username = FIELD_USERNAME
    email = FIELD_EMAIL
    last_name = FIELD_LAST_NAME
    first_name = FIELD_FIRST_NAME
    password = FIELD_PASSWORD
    confirm_password = FIELD_CONFIRM

class GroupRegisterForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class OldGroupRegisterForm(forms.Form):
    email = FIELD_EMAIL
    group_name = FIELD_GROUP_NAME
    # phone = FIELD_PHONE
    members = FIELD_MEMBERS
    musical_style = FIELD_MUSICAL_STYLE
    diet = FIELD_DIET
    facebook = FIELD_FACEBOOK
    instagram = FIELD_INSTAGRAM
    twitter = FIELD_TWITTER
    participants = FIELD_PARTICIPANTS
    biography = FIELD_BIOGRAPHY

class ConcertForm(forms.Form):
    group_name = FIELD_GROUP_NAME
    members = FIELD_MEMBERS
    email = FIELD_EMAIL
    musical_style = FIELD_MUSICAL_STYLE
    facebook = FIELD_FACEBOOK
    instagram = FIELD_INSTAGRAM
    twitter = FIELD_TWITTER
    diet = FIELD_DIET
    biography = FIELD_BIOGRAPHY

"""
    Replaced django.contrib.auth.forms fields
"""
class UserPasswordResetForm(PasswordResetForm):
    email = FIELD_EMAIL

class UserPasswordSetForm(SetPasswordForm):
    new_password1 = FIELD_PASSWORD
    new_password2 = FIELD_CONFIRM
