from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, IDFilter


async def cmd_start(message: types.Message, state: FSMContext):
    """Обработка команды /start

    :param message: объект message
    :param state: объект state
    :return:
    """
    await state.finish()
    await message.answer('Для заказа еды нажмите /food', reply_markup=types.ReplyKeyboardRemove())


async def cmd_cancel(message: types.Message, state: FSMContext):
    """Обработка команды /cancel

    :param message: объект message
    :param state: объект state
    :return:
    """
    await state.finish()
    await message.answer('Действие отменено', reply_markup=types.ReplyKeyboardRemove())


def register_handlers_common(dp: Dispatcher):
    """Функция регистрации хэндлеров

    :param dp: объект Dispatcher-а
    :return:
    """
    dp.register_message_handler(cmd_start, commands='start', state='*')
    dp.register_message_handler(cmd_cancel, commands='cancel', state='*')
    dp.register_message_handler(cmd_start, Text(equals='отмена', ignore_case=True), state='*')

