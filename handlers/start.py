# handlers/start.py
from aiogram import types
from aiogram.dispatcher import Dispatcher

async def send_welcome(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    welcome_message = f"Привет, {user_name}! Ваш ID: {user_id}"
    await message.reply(welcome_message)

def register_handlers_start(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands="start")
