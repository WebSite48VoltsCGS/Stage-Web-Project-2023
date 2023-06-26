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
from django.contrib.auth import views as auth_views
from studios import views
from studios.forms import UserPasswordResetForm, UserPasswordSetForm

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # WIP
    path('', views.placeholder, name='placeholder'),

    # Main
    path('', views.home, name='home'),
    path('actualites/', views.news, name='news'),
    path('studios/', views.studios, name='studios'),
    path('bar/', views.bar, name='bar'),
    path('espace_pro/', views.pro_area, name='pro_area'),
    path('contact/', views.contact, name='contact'),
    path('reservation/', views.booking, name='booking'),

    # Account
    path('compte/connexion/', views.account_sign_in, name='account-sign_in'),
    path('compte/inscription/', views.account_sign_up, name='account-sign_up'),
    path('compte/deconnexion/', views.account_log_out, name='account-logout'),

    # Profile
    path('compte/mon_profil/', views.profile_detail, name='profile-detail'),
    path('compte/mon_profil/modifier/', views.profile_update, name='profile-update'),
    path('compte/mon_profil/modifier/username', views.profile_username_update, name='profile_username-update'),
    path('compte/mon_profil/modifier/email', views.profile_email_update, name='profile_email-update'),
    path('compte/mon_profil/modifier/password', views.profile_password_update, name='profile_password-update'),

    # Groups
    path('compte/mes_groupes/', views.groups_detail, name='groups-detail'),
    path('compte/mes_groupes/ajouter/', views.groups_create, name='groups-create'),
    path('compte/mes_groupes/modifier/', views.groups_update, name='groups-update'),
    path('compte/mes_groupes/supprimer/', views.groups_delete, name='groups-delete'),

    # Bookings
    path('compte/mes_reservations/', views.bookings_detail, name='bookings-detail'),
    path('compte/mes_reservations/ajouter/', views.bookings_create, name='bookings-create'),

    # Forgot password
    path('compte/mot-de-passe-oublie/',
         auth_views.PasswordResetView.as_view(
             template_name='forgot_password_form.html',
             form_class=UserPasswordResetForm),
         name='forgot_password-form'),
    path('compte/mot-de-passe-oublie/envoi/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='forgot_password_done.html'),
         name='forgot_password-done'),
    path('compte/mot-de-passe-oublie/modification/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='forgot_password_confirm.html',
             form_class=UserPasswordSetForm),
         name='forgot_password-confirm'),
    path('compte/mot-de-passe-oublie/confirmation/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='forgot_password_complete.html'),
         name='forgot_password-complete'),
]
