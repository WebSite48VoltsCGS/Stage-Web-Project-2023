"""
URL configurations

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('accueil/', views.home, name='home'),
    path('actualités/', views.news, name='news'),
    path('studios/', views.studios, name='studios'),
    path('bar/', views.bar, name='bar'),
    path('espace_pro/', views.pro_area, name='pro_area'),
    path('contact/', views.contact, name='contact'),
    path('réservation/', views.booking, name='booking'),
    path('compte/<int:account_id>/', views.account_detail, name='account-detail'),
    path('se_connecter/', views.sign_in, name='sign_in'),
    path('créer_un_compte/', views.sign_up, name='sign_up'),
]
