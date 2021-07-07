from django.db import models

# Create your models here.

# ! obtener datos de la carta
class Card(models.Model):
    name = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    value = models.IntegerField()
    image = models.BinaryField()

    class Meta:
        db_table = 'card'

    def __repr__(self):
        return "name='%s', series='%s', value='%s', image='https://ruka.life/card/%s/image.jpg'" % (self.name, self.series, self.value, self.id)


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    balance = models.IntegerField()
    created_at = models.DateField()
    capacity = models.IntegerField()
    suscription = models.CharField(max_length=60)

    class Meta:
        managed = True
        db_table = 'person'
    
    def __repr__(self):
        return "user_id= '%s', balance='%s', created_at='%s', capacity='%s', suscription='%s'" % (self.user_id, self.balance, self.created_at, self.capacity, self.suscription)

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

    def __repr__(self):
        return "card_id= '%s', code_id= '%s', durability= '%s', favorite= '%s', owner_id= '%s', number= '%s'" % (self.card_id, self.code_id, self.durability, self.favorite, self.owner_id, self.number)
