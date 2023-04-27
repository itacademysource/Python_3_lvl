import os

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from translater import RuEnTranslater

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands='start')  # Декоратор, "отлавливающий" только команду /start
async def start_message(message: types.Message):
    """Функция, работающая после команды /start

    :param message: types.Message
    :return:
    """
    await message.answer('Привет, я бот который может преобразовать русский текст, написанный английской раскладкой')


@dp.message_handler()  # Декоратор, "отлавливающий" все сообщения
async def translate(message: types.Message):
    """Функция перевода

    :param message: types.Message
    :return:
    """
    try:
        text = RuEnTranslater(message.text)  # Вызываем функцию перевода и передаем туда текст
        await message.reply(str(text))
    except Exception as ex:
        await message.reply(str(repr(ex)))  # Отправляем ошибку в случае ее возникновения


if __name__ == '__main__':
    print('bot started')
    executor.start_polling(dp, skip_updates=True)
