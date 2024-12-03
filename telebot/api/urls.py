from django.urls import path
from .views import callback, index, telegram_login

urlpatterns = [
    path('', index),
    path('telegram_login/', telegram_login, name='telegram_login'),
    path('callback/', callback, name='callback'),
]
