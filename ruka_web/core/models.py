from django.db import models

# Create your models here.

class card(models.Model):
    name = models.CharField(max_length=255)
    series = models.CharField(max_length=255)
    value = models.IntegerField()
    image = models.BinaryField()

    class Meta:
        db_table = 'card'

    def __repr__(self):
        return "name='%s', series='%s', value='%s', image='%s'" % (self.name, self.series, self.value, self.image)
