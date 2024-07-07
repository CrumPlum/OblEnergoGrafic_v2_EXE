# handlers/__init__.py
from aiogram import Dispatcher
from .start import register_handlers_start
from .help import register_handlers_help
from .file import register_handlers_file

def register_handlers(dp: Dispatcher):
    register_handlers_start(dp)
    register_handlers_help(dp)
    register_handlers_file(dp)
