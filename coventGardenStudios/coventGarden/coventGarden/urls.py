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

    # Main
    path('', views.home, name='home'),
    path('actualites/', views.news, name='news'),
    path('studios/', views.studios, name='studios'),
    path('bar/', views.bar, name='bar'),
    path('espace_pro/', views.pro_area, name='pro_area'),
    path('contact/', views.contact, name='contact'),
    path('reservation/', views.booking, name='booking'),

    # Account
    path('compte/profil', views.account, name='account'),
    path('compte/connexion/', views.sign_in, name='sign_in'),
    path('compte/inscription/', views.sign_up, name='sign_up'),

    # Forgot password
    path('compte/mot-de-passe-oublie/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset_form.html',
             form_class=UserPasswordResetForm),
         name='password_reset'),
    path('compte/mot-de-passe-oublie/envoi/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'),
         name='password_reset_done'),
    path('compte/mot-de-passe-oublie/modification/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html',
             form_class=UserPasswordSetForm),
         name='password_reset_confirm'),
    path('compte/mot-de-passe-oublie/confirmation/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

    # Group
    path('compte/groupe/', views.group_detail, name='group-detail'),
    path('compte/groupe/inscription', views.group_register, name='group-register'),

]
