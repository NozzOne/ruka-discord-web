from django.shortcuts import render, get_object_or_404
from .models import card
from django.http import HttpResponse
import base64

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def comandos(request):

    return render(request, 'core/comandos.html')

def get_card(request, image_id):
    obj = card.objects.get(id=image_id)
    value = obj.image
    image = bytes(value)
    return HttpResponse(image, content_type='image/jpeg')

