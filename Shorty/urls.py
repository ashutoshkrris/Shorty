"""Shorty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from authentication.views import loginPage, signup, logout, passwordChange
from URLHandler.views import dashboard, generate, home, deleteurl
from home_shorty.views import short_generate,home_shortener
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('signup/', signup, name="signup"),
    path('loginPage/', loginPage, name="loginPage"),
    path('logout/', logout, name="logout"),
    path('passwordChange/', passwordChange, name="passwordChange"),
    path('dashboard/', dashboard, name="dashboard"),
    path('url_shorten/',home_shortener,name="home_shortener"),
    path('generate/', generate, name="generate"),
    path('shorten/',short_generate,name="shorten"),
    path('deleteurl/', deleteurl, name="deleteurl"),
    path('<str:query>/', home, name="home"),
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
]
