from django.contrib import admin
from .models import User, Card, Cardinstance

# Register your models here.
admin.site.register(User)
admin.site.register(Card)
admin.site.register(Cardinstance)
