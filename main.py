# main.py
import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from config import TOKEN #создаем файл config.py c TOKEN = 'yourToken'
from handlers import register_handlers

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Регистрация middlewares
dp.middleware.setup(LoggingMiddleware())

# Регистрация обработчиков
register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
