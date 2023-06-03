from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, reverse
from .models import Card, Cardinstance, Inventory, Shop
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from colorthief import ColorThief
import requests, io


def home(request):
    if 'user' in request.session:
        
        data = request.session['user']
        return render(request, 'core/home.html', {"user": data})
    else:
        return render(request, 'core/home.html')

def comandos(request):
    return render(request, 'core/comandos.html')


def user(request, id):
    data = request.session['user']
    if data['avatar'] is None:
        r = requests.get("https://discord.com/assets/1f0bfc0865d324c2587920a7d80c609b.png")
    else:
        r = requests.get(f'https://cdn.discordapp.com/avatars/{data["id"]}/{data["avatar"]}.webp?size=256')
        
    f = io.BytesIO(r.content)
    color_thief = ColorThief(f)
    color = color_thief.get_color(quality=1)


    cards = Cardinstance.objects.select_related('card').filter(owner=id).values('card_id','code_id',  'card__name', 'card__series', 'durability', 'favorite', 'owner', 'number')

    return render(request, 'core/user.html', {"user": data, "cards": cards, "color": color})



def logout(request):
    del request.session['user']
    return redirect(home)

def get_cardimage(request, id):
    obj = Card.objects.get(card_id=id)
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
        "client_id": "",
        "client_secret": "",
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