from django.contrib.auth.models import User
from django.db import models

from .constants import ID_MAX_LENGTH, USERNAME_MAX_LENGTH

class TelegramUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    telegram_id = models.CharField(
        max_length=ID_MAX_LENGTH
    )
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        null=True, blank=True,
    )
