from rest_framework import serializers
from core.models import Card, Cardinstance, User

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields =  ['name', 'series', 'value', 'image']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'balance', 'created_at', 'capacity', 'suscription']

class CardInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cardinstance
        fields = ['card_id', 'code_id', 'durability', 'favorite', 'owner_id', 'number']