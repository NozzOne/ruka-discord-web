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
    favorite = models.CharField(max_length=1,null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.BigIntegerField(null=False)

    class Meta:
        managed = True
        db_table = 'cardinstance'
        
    def __str__(self):
        return self.code_id, self.card, self.favorite, self.owner, self.number

class Shop(models.Model):
    item_id = models.IntegerField(primary_key=True)
    emoji = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    description = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'shop'
    def __str__(self):
        return self.item_id, self.name, self.cost, self.description

class Inventory(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    amount = models.IntegerField()


    class Meta:
        managed = True
        db_table = 'inventory'
    
    def __str__(self):
        return self.owner_id, self.item_id, self.amount

class Guild(models.Model):
    guild_id = models.BigIntegerField(primary_key=True)
    prefix = models.CharField(max_length=3)

    class Meta:
        managed = True
        db_table = 'guild'
    
    def __str__(self):
        return '{} {}'.format(self.guild_id, self.prefix)


class Shard(models.Model):
    shard_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    shard_ping = models.IntegerField()
    shard_servers = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'shards'

    def __str__(self):
        return self.shard_id, self.name, self.status, self.shard_ping, self.shard_servers
    