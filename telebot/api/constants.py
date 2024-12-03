import os
from dotenv import load_dotenv

load_dotenv()

TOKEN=os.getenv('TOKEN')
TELEGRAM_BOT=os.getenv('TELEGRAM_BOT')
ID_MAX_LENGTH=255
USERNAME_MAX_LENGTH=255
