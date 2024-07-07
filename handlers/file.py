# handlers/file.py
import os
import requests
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InputFile
from bs4 import BeautifulSoup

async def send_file(message: types.Message):
    url = 'https://zakarpat.energy/customers/break-in-electricity-supply/schedule/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tag = soup.select_one('.container2 img[src*="timetable-now"]')
    img_url = 'https://zakarpat.energy' + img_tag['src']

    img_data = requests.get(img_url).content
    with open('grafik0.png', 'wb') as handler:
        handler.write(img_data)

    await message.reply_photo(InputFile('grafik0.png'), caption="Вот ваше изображение")

def register_handlers_file(dp: Dispatcher):
    dp.register_message_handler(send_file, commands="file")
