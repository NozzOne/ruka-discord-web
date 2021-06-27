from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('comandos', views.comandos ,name="comandos"),
    path('card/<int:image_id>/image.jpg', views.get_card, name="carta")
]
