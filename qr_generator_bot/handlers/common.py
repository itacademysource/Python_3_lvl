import logging
from aiogram import Bot, Dispatcher, executor, types
import pyqrcode as pq

from config_reader import load_config

config = load_config(r'D:\PycharmProjects\Pt9\bots\food_bot\config\bot_config.ini')

TOKEN = config.tg_bot.token

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет, я бот, который сделает QR-код из любой твоей ссылки')


@dp.message_handler()
async def translate_func(message: types.Message):
    try:
        await message.answer('Создаю QR-код...')
        qr_code = pq.create(message.text)
        qr_code.png('code.png', scale=6)

        with open('code.png', 'rb') as photo:
            await bot.send_photo(message.chat.id, photo)
            await message.answer('Ваш QR-код готов!')
    except Exception as ex:
        logging.error(repr(ex))
        await message.answer('Я не могу создать QR-код. Пожалуйста, введите корректную ссылку')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
