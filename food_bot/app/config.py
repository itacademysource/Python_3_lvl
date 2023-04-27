from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config_reader import load_config


bot_config = load_config(r'D:\PycharmProjects\Pt9\bots\food_bot\config\bot_config.ini')

bot = Bot(token=bot_config.tg_bot.token)
dp = Dispatcher(bot, storage=MemoryStorage())
