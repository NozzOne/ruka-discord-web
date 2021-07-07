from django.urls import path
from rukarest import views
from rukarest.viewslogin import login

urlpatterns = [
    path('users', views.usuarios_lista, name="Lista de usuarios"),
    path('user_cards/<id>', views.cartas_usuario, name="Cartas del usuario"),
    path('getcard/<id>', views.getcard, name="Obtener carta"),
    path('login', login, name="Login"),
]