from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .constants import TOKEN, TELEGRAM_BOT
from .models import TelegramUser


def index(request):
    return render(request, 'api/index.html')

def telegram_login(request):
    token = TOKEN
    #telegram_url = f'https://t.me/{TELEGRAM_BOT}/auth/complete/telegram'
    telegram_url = f'https://t.me/{TELEGRAM_BOT}?start=start'
    return redirect(telegram_url)

@login_required
def callback(request):
    token = request.GET.get('token')
    telegram_user = TelegramUser.objects.get(telegram_id=token)
    if telegram_user:
        telegram_user.user = request.user
        telegram_user.save()
        return redirect('home')
