from django import forms
from django.db import models

# Global variables
LENGTH_NAME = 150
LENGTH_PASSWORD = 150
LENGTH_EMAIL = 320

# Labels
LABEL_USERNAME = "Nom d'utilisateur"
LABEL_FIRST_NAME = "Prénom"
LABEL_LAST_NAME = "Nom"
LABEL_GROUP_NAME = "Nom de groupe"
LABEL_EMAIL = "Adresse e-mail"
LABEL_PASSWORD = "Mot de passe"
LABEL_CONFIRM = "Confirmer le mot de passe"

# Widgets
WIDGET_TEXT = forms.TextInput(attrs={'class': 'form-control'})
WIDGET_EMAIL = forms.EmailInput(attrs={'class': 'form-control'})
WIDGET_PASSWORD = forms.PasswordInput(attrs={'class': 'form-control'})

# Forms
FORM_USERNAME = forms.CharField(max_length=LENGTH_NAME, label=LABEL_USERNAME, widget=WIDGET_TEXT)
FORM_FIRST_NAME = forms.CharField(max_length=LENGTH_NAME, label=LABEL_FIRST_NAME, widget=WIDGET_TEXT)
FORM_LAST_NAME = forms.CharField(max_length=LENGTH_NAME, label=LABEL_LAST_NAME, widget=WIDGET_TEXT)
FORM_GROUP_NAME = forms.CharField(max_length=LENGTH_NAME, label=LABEL_GROUP_NAME, widget=WIDGET_TEXT)
FORM_EMAIL = forms.EmailField(max_length=LENGTH_EMAIL, label=LABEL_EMAIL, widget=WIDGET_EMAIL)
FORM_PASSWORD = forms.CharField(max_length=LENGTH_PASSWORD, label=LABEL_PASSWORD, widget=WIDGET_PASSWORD)
FORM_CONFIRM = forms.CharField(max_length=LENGTH_PASSWORD, label=LABEL_CONFIRM, widget=WIDGET_PASSWORD)

# Models
MODEL_USERNAME = models.CharField(max_length=LENGTH_NAME)
MODEL_FIRST_NAME = models.CharField(max_length=LENGTH_NAME)
MODEL_LAST_NAME = models.CharField(max_length=LENGTH_NAME)
MODEL_GROUP_NAME = models.CharField(max_length=LENGTH_NAME)
MODEL_EMAIL = models.EmailField(max_length=LENGTH_EMAIL)
MODEL_PASSWORD = models.CharField(max_length=LENGTH_PASSWORD)
MODEL_CONFIRM = models.CharField(max_length=LENGTH_PASSWORD)

MODELS_TEST = models.CharField(max_length=LENGTH_NAME, default="Test")
