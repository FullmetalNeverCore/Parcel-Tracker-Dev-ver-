import aiogram
from aiogram import Bot, Dispatcher, executor, md, types
import os 
import sys 
import logging 
import trackparcel 
from trackparcel import *


token = "1131623077:AAEa_6_kNrg50u9auBdnaZdiwDQtHIMYb5U"
api = Bot(token=token, parse_mode=types.ParseMode.MARKDOWN)
disp = Dispatcher(api)
logging.basicConfig(level=logging.INFO)

@disp.message_handler(commands=['track'])
async def track(message: types.Message):
    id = message.from_user.id
    mt = message.text 
    print(message.text)
    mt2 = mt.split("-")
    await trackparcel.url_creator(mt2[1], id)

async def send_msg(msg, id):
    print(msg)
    await api.send_message(int(id), msg)

if __name__ == '__main__':
    executor.start_polling(disp, skip_updates=True)