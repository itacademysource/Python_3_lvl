import logging

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher

from config import load_config
from databases.sqlite_db import SQLiteDB

storage = MemoryStorage()

logger = logging.getLogger(__name__)

config = load_config(r'config/config.ini')

reminder_bot_db = SQLiteDB()

TOKEN = config.tg_bot.BOT_TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)
