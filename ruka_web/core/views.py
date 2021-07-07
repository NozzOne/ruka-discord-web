from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, reverse
from .models import Card
import requests

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def comandos(request):
    return render(request, 'core/comandos.html')

def user(request, id):
    user_data = request.session['user']
    return render(request, 'core/user.html', {"user": user_data['username']})

def get_cardimage(request, image_id):
    obj = Card.objects.get(id=image_id)
    value = obj.image
    image = bytes(value)
    return HttpResponse(image, content_type='image/jpeg')

auth_url_discord = "https://discord.com/api/oauth2/authorize?client_id=749462161713266738&redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify"

def discord_login(request: HttpResponse):
    return redirect(auth_url_discord)

def discord_login_redirect(request: HttpResponse):
    code = request.GET.get('code')
    user = exchange_code(code)
    request.session['user'] = user
    return redirect(f'/user/{user["id"]}')


def exchange_code(code: str):
    data = {
        "client_id": "749462161713266738",
        "client_secret": "2JuGhx1CMMumcA-uK-ROuP0XISP6EEY7",
        'grant_type': 'authorization_code',
        "code": code,
        "redirect_uri": "http://127.0.0.1:8000/oauth2/login/redirect",
        "scope": "identify"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post("https://discord.com/api/oauth2/token", data=data, headers=headers)
    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': 'Bearer %s' % access_token})
    user = response.json()
    return user