# handlers/help.py
from aiogram import types
from aiogram.dispatcher import Dispatcher

async def send_help(message: types.Message):
    help_text = (
        "Доступные команды:\n"
        "/start - Запустить бота\n"
        "/help - Получить помощь\n"
        "/file - Получить файл grafik0.png"
    )
    await message.reply(help_text)

def register_handlers_help(dp: Dispatcher):
    dp.register_message_handler(send_help, commands="help")
