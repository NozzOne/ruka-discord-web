from rest_framework import response
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Card, Cardinstance, User, Shard
from .serializers import ShardCloseSerializer, UserSerializer, CardSerializer, CardInstanceSerializer, ShardUpdateSerializer

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

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def getcard(request, id):
    try:
        carta = Card.objects.filter(card_id=id)
    except Shard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CardSerializer(carta, many=True)
        return Response(serializer.data)


@csrf_exempt
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def update_shard(request, name):
    try:
        shard = Shard.objects.get(name= name)
    except Shard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ShardUpdateSerializer(shard, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def close_shard(request, name):
    try:
        shard = Shard.objects.get(name= name)
    except Shard.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ShardCloseSerializer(shard, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
