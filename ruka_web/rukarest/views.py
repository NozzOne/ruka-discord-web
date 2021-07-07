from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Card, Cardinstance, User
from .serializers import UserSerializer, CardSerializer, CardInstanceSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def usuarios_lista(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
        
@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def cartas_usuario(request, id):
    if request.method == 'GET':
        user = Cardinstance.objects.filter(owner=id)
        serializer = CardInstanceSerializer(user, many=True)
        return Response(serializer.data)

# SELECT 
#     c.id,
#     c.name,
#     c.series,
#     c.value,
#     ci.code_id,
#     ci.favorite,
#     ci.durability
# FROM cardinstance ci 
# INNER JOIN card c ON ci.card_id = c.id
# WHERE OWNER_ID = ci.owner_id