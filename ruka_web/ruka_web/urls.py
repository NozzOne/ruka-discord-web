"""ruka_web URL Configuration

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
from core import views


handler404 = 'core.views.Errorhandler404'
handler500 = 'core.views.Errorhandler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),   
    path('oauth2/login', views.discord_login, name="oauth_login"),
    path('oauth2/login/redirect', views.discord_login_redirect, name="discord_login_redirect"),
    path('api/v1/', include('rukarest.urls'))
]
