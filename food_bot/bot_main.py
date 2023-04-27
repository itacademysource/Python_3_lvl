import asyncio
import logging

from aiogram import Bot
from aiogram.types import BotCommand

from app.handlers import food_handlers, drink_handlers, common_handlers

from config import bot, dp

logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    """Создание меню бота

    :param bot: экземпляр класса bot
    :return:
    """
    commands = [
        BotCommand(command='/start', description='Начало работы'),
        BotCommand(command='/food', description='Выбор еды'),
        BotCommand(command='/drink', description='Выбор напитков'),
        BotCommand(command='/cancel', description='Отмена')
    ]

    await bot.set_my_commands(commands)


async def main():
    """Запуск бота

    :return:
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger.info('Starting bot')

    """Регистрация хэндлеров"""
    common_handlers(dp)
    food_handlers(dp)
    drink_handlers(dp)

    await set_commands(bot)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
