from django.urls import path
from rukarest import views
from rukarest.viewslogin import login

urlpatterns = [
    path('users', views.usuarios_lista, name="Lista_de_usuarios"),
    path('user_cards/<id>', views.cartas_usuario, name="Cartas_del_usuario"),
    path('getcard/<id>', views.getcard, name="Obtener_carta"),
    path('login', login, name="Login"),
    path('update_shard/<name>', views.update_shard, name="Actualizar_shard"),
    path('close_shard/<name>', views.close_shard, name="Cerrar_shard")
]