"""coventGarden URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from studios import views
from studios.forms import UserPasswordResetForm, UserPasswordSetForm
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # WIP
    path('', views.placeholder, name='placeholder'),

    # Navigation
    path('', views.home, name='home'),
    path('actualites/', views.news, name='news'),
    path('studios/', views.studios, name='studios'),
    path('bar/', views.bar, name='bar'),
    path('espace_pro/', views.pro_area, name='pro_area'),
    path('contact/', views.contact, name='contact'),
    path('reservation/', views.booking, name='booking'),

    # Account
    path('compte/connexion/', views.account_sign_in, name='account_sign_in'),
    path('compte/inscription/', views.account_sign_up, name='account_sign_up'),
    path('compte/deconnexion/', views.account_log_out, name='account_log_out'),

    # Profile
    path('compte/mon_profil/', views.profile_detail, name='profile_detail'),
    path('compte/mon_profil/modifier/', views.profile_update, name='profile_update'),
    path('compte/mon_profil/modifier/nom_utilisateur', views.profile_username_update, name='profile_username_update'),
    path('compte/mon_profil/modifier/email', views.profile_email_update, name='profile_email_update'),
    path('compte/mon_profil/modifier/mot_de_passe', views.profile_password_update, name='profile_password_update'),

    # Groups
    path('compte/mes_groupes/', views.groups_detail, name='groups_detail'),
    path('compte/mes_groupes/ajouter/', views.groups_create, name='groups_create'),
    path('compte/mes_groupes/modifier/', views.groups_update, name='groups_update'),
    path('compte/mes_groupes/supprimer/', views.groups_delete, name='groups_delete'),

    # Bookings
    path('compte/mes_reservations/', views.bookings_detail, name='bookings_detail'),
    path('compte/mes_reservations/ajouter/', views.bookings_create, name='bookings_create'),

    # Password Reset
    path('compte/mot-de-passe/oublie/',
         PasswordResetView.as_view(
             template_name='password_reset/password_reset_forgot.html',
             html_email_template_name='password_reset/password_reset_email.html',
             form_class=UserPasswordResetForm),
         name='password_reset_forgot'),
    path('compte/mot-de-passe-oublie/envoi/',
         PasswordResetDoneView.as_view(
             template_name='password_reset/password_reset_done.html'),
         name='password_reset_done'),
    path('compte/mot-de-passe-oublie/modification/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='password_reset/password_reset_confirm.html',
             form_class=UserPasswordSetForm),
         name='password_reset_confirm'),
    path('compte/mot-de-passe-oublie/confirmation/',
         PasswordResetCompleteView.as_view(
             template_name='password_reset/password_reset_complete.html'),
         name='password_reset_complete'),
]
