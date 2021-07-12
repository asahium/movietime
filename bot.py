import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text
from kinodef import search
from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

##

Start_message = text(
    "Привет 👋",
    "На связи бот @movieproject_bot! Как я могу тебе помочь?",
    sep="\n"
)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(Start_message, reply_markup=kb.markup_start)

##

help_message = text(
    "Это бот советчик по фильмам",
    "Доступные команды:\n",
    "/start - приветствие",
    "/secret - нажми на меня",
    sep="\n"
)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)

@dp.message_handler(commands=['secret'])
async def process_help_command(message: types.Message):
    await message.reply(text="Тык", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLxb0XwjhqM_RLETkiOkUZrEE8K-fP3V-p&index=3")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await msg.reply(msg.from_user.id, msg.text)
#    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
