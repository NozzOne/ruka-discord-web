from django.urls import path
from .views import home, comandos

urlpatterns = [
    path('', home, name="home"),
    path('comandos',comandos,name ="comandos"),
]
