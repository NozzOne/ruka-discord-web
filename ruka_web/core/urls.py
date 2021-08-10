from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('comandos', views.comandos ,name="comandos"),
    path('card/<int:id>/image.jpg', views.get_cardimage, name="card_image"),
    path('card/<int:id>/<int:calidad>/image.jpg', views.get_image, name="get_image"),
    path('user/<int:id>', views.user, name="coleccion"),
    path('logout', views.logout, name="logout"),
    path('status', views.status, name="status"),
]
