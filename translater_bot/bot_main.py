from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from translater import translater

bot = Bot(os.environ.get('TOKEN'))  # Токен бота, полученный у @BotFather в Telegram
dp = Dispatcher(bot)  # Экземпляр класса диспетчера


@dp.message_handler(commands='start')  # Хэндлер, реагирующий на команду /start
async def start_message(message: types.Message):
    """Функция, отвечающая пользователю после введения команды /start

    :param message: types.Message
    :return:
    """
    await bot.send_message(message.from_user.id,
                           'Привет, введи текст на русском и я переведу его на английский')  # Отправка сообщения


@dp.message_handler()
async def echo(message: types.Message):
    """Функция, переводящая полученный текст

    :param message: types.Message
    :return:
    """
    translation_result = translater(text=message.text)  # Переводим текст
    await message.answer(str(translation_result))  # Отправляем переведенный текст пользователю


if __name__ == '__main__':
    """Запуск бота"""

    print('bot polling started')
    executor.start_polling(dp, skip_updates=True)
