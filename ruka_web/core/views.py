from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Card, Cardinstance, User, Guild, Shard
from django.db.models import Sum
from django.core.files.uploadedfile import InMemoryUploadedFile

from colorthief import ColorThief
import requests, io
from PIL import Image, ImageDraw, ImageFilter, ImageChops


def home(request):
    if 'user' in request.session:
        
        data = request.session['user']
        return render(request, 'core/home.html', {"user": data})
    else:
        return render(request, 'core/home.html')

def comandos(request):
    return render(request, 'core/comandos.html')


def user(request, id):
    try:
        data = request.session['user']

        if data['id'] == id:
            if data['avatar'] is None:
                r = requests.get("https://discord.com/assets/1f0bfc0865d324c2587920a7d80c609b.png")
            else:
                r = requests.get(f'https://cdn.discordapp.com/avatars/{data["id"]}/{data["avatar"]}.webp?size=256')
                
            f = io.BytesIO(r.content)
            color_thief = ColorThief(f)
            color = color_thief.get_color(quality=1)


            cards = Cardinstance.objects.select_related('card').filter(owner=id).values('card_id','code_id',  'card__name', 'card__series', 'favorite', 'owner', 'number')

            return render(request, 'core/user.html', {"user": data, "cards": cards, "color": color})
        elif data['id'] != id:
            response = requests.get(f'https://discord.com/api/v8/users/{id}', headers={'Authorization': f'Bot NzQ5NDYyMTYxNzEzMjY2NzM4.X0sVBw.JdwE5vBF5cSwvgs2gqGHEq3_ELs'})
            user = response.json()

            if user['avatar'] is None:
                r = requests.get("https://discord.com/assets/1f0bfc0865d324c2587920a7d80c609b.png")
            else:
                r = requests.get(f'https://cdn.discordapp.com/avatars/{user["id"]}/{user["avatar"]}.webp?size=256')
                
            f = io.BytesIO(r.content)
            color_thief = ColorThief(f)
            color = color_thief.get_color(quality=1)


            cards = Cardinstance.objects.select_related('card').filter(owner=id).values('card_id','code_id',  'card__name', 'card__series', 'favorite', 'owner', 'number')

            return render(request, 'core/user.html', {"user": user, "cards": cards, "color": color})
    except:
        response = requests.get(f'https://discord.com/api/v8/users/{id}', headers={'Authorization': f'Bot NzQ5NDYyMTYxNzEzMjY2NzM4.X0sVBw.JdwE5vBF5cSwvgs2gqGHEq3_ELs'})
        user = response.json()

        if user['avatar'] is None:
            r = requests.get("https://discord.com/assets/1f0bfc0865d324c2587920a7d80c609b.png")
        else:
            r = requests.get(f'https://cdn.discordapp.com/avatars/{user["id"]}/{user["avatar"]}.webp?size=256')
            
        f = io.BytesIO(r.content)
        color_thief = ColorThief(f)
        color = color_thief.get_color(quality=1)


        cards = Cardinstance.objects.select_related('card').filter(owner=id).values('card_id','code_id',  'card__name', 'card__series', 'favorite', 'owner', 'number')

        return render(request, 'core/user.html', {"user": user, "cards": cards, "color": color})

def status(request):
    usuarios = User.objects.count()
    servidores = Shard.objects.aggregate(Sum('shard_servers'))

    try:
        obj = Shard.objects.first()
        field_object = Shard._meta.get_field('status')
        ready = field_object.value_from_object(obj)
    except Shard.DoesNotExist:
        ready = 'Desconectado'

    def get_shard_count():
        data = requests.get('https://discordapp.com/api/v8/gateway/bot', headers={
        "Authorization": "Bot NzQ5NDYyMTYxNzEzMjY2NzM4.X0sVBw.JdwE5vBF5cSwvgs2gqGHEq3_ELs",
        "User-Agent": "DiscordBot (https://github.com/Rapptz/discord.py 1.3.0a) Python/3.7 aiohttp/3.6.1"
    })
        data.raise_for_status()
        content = data.json()
        # return 16
        return content['shards']
    shards = get_shard_count()
    shards_list = Shard.objects.all().order_by('shard_id')

    return render(request, 'core/status.html', {"users": usuarios, "guilds": servidores, "shards": shards, "shard_list": shards_list, "status": ready})

def logout(request):
    if 'user' not in request.session:
        return redirect(home)
    else:
        del request.session['user']
        return redirect(home)

def get_cardimage(request, id):
    obj = Card.objects.get(card_id=id)
    value = obj.image
    image = bytes(value)
    
    return HttpResponse(image, content_type='image/jpeg')

auth_url_discord = "https://discord.com/api/oauth2/authorize?client_id=749462161713266738&redirect_uri=https%3A%2F%2Fruka.life%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify"

def get_image(request, id, calidad):
    im1 = Image.open(requests.get(url=f'https://ruka.life/card/{id}/image.jpg', stream=True).raw).convert('RGBA')
    im2 = Image.open(requests.get(url='https://i.imgur.com/VIJgbnK.png', stream=True).raw).convert('RGBA').filter(ImageFilter.UnsharpMask)
    bands = list(im2.split())
    if len(bands) == 4:
        # Assuming alpha is the last band
        bands[3] = bands[3].point(lambda x: x*float(str(f"0.{calidad}")))
    im2 = Image.merge(im2.mode, bands)

    im1.paste(im2, (0,0), im2)
    response = HttpResponse(content_type='image/PNG')
    im1.save(response, format='PNG')

    return response

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
        "redirect_uri": "https://ruka.life/oauth2/login/redirect",
        "scope": "identify"
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post("https://discord.com/api/v8/oauth2/token", data=data, headers=headers)
    credentials = response.json()
    access_token = credentials['access_token']
    response = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': f'Bearer {access_token}'})
    user = response.json()
    return user