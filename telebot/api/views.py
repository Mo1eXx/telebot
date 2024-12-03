from django.shortcuts import redirect, render

from .constants import TOKEN, TELEGRAM_BOT

def index(request):
    return render(request, 'api/index.html')

def telegram_login(request):
    token = TOKEN
    #telegram_url = f'https://t.me/{TELEGRAM_BOT}/auth/complete/telegram'
    telegram_url = f'https://t.me/{TELEGRAM_BOT}?start=start'
    return redirect(telegram_url)
