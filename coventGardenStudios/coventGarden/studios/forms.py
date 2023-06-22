from django import forms

# Global variables
LENGTH_NAME = 256
LENGTH_PASSWORD = 256
LENGTH_EMAIL = 320

# Fields
FIELD_USERNAME = forms.CharField(max_length=LENGTH_NAME, label="Nom d'utilisateur")
FIELD_EMAIL = forms.EmailField(max_length=LENGTH_EMAIL, label="Adresse e-mail")
FIELD_PASSWORD = forms.CharField(max_length=LENGTH_PASSWORD, label="Mot de passe", widget=forms.PasswordInput)
FIELD_CONFIRM = forms.CharField(max_length=LENGTH_PASSWORD, label="Confirmer le mot de passe", widget=forms.PasswordInput)
FIELD_FIRST_NAME = forms.CharField(max_length=LENGTH_NAME, label="Prénom")
FIELD_LAST_NAME = forms.CharField(max_length=LENGTH_NAME, label="Nom")

# Register your forms here
class SignUpForm(forms.Form):
    username = FIELD_USERNAME
    email = FIELD_EMAIL
    first_name = FIELD_FIRST_NAME
    last_name = FIELD_LAST_NAME
    password = FIELD_PASSWORD
    confirm_password = FIELD_CONFIRM

    # Class = 'form-control'
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class SignInForm(forms.Form):
    username = FIELD_USERNAME
    password = FIELD_PASSWORD

    # Class = 'form-control'
    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class PasswordResetForm(forms.Form):
    email = FIELD_EMAIL

    # Class = 'form-control'
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
