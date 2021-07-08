from django.db import models

# Create your models here.

# ! obtener datos de la carta
class Card(models.Model):
    card_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    value = models.IntegerField()
    image = models.BinaryField()

    class Meta:
        managed = True
        db_table = 'card'
    def __str__(self):
        return self.card_id, self.name, self.value, self.image

class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    balance = models.IntegerField()
    created_at = models.DateField()
    capacity = models.IntegerField()
    suscription = models.CharField(max_length=60)

    class Meta:
        managed = True
        db_table = 'person'
    
    def __str__(self):
        return self.user_id, self.balance, self.created_at, self.capacity, self.suscription

class Cardinstance(models.Model):
    code_id = models.CharField(primary_key=True, max_length=6)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    durability = models.IntegerField(null=False)
    favorite = models.CharField(max_length=1,null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.BigIntegerField(null=False)

    class Meta:
        managed = True
        db_table = 'cardinstance'
        
    def __str__(self):
        return self.code_id, self.card, self.durability, self.favorite, self.owner, self.number
        