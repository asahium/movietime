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
    "Для справки /help",
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
    "/search - поиск фильма",
    "/secret - нажми на меня",
    sep="\n"
)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)

##

@dp.message_handler(commands=['secret'])
async def process_secret_command(message: types.Message):
    await message.reply(reply_markup=kb.secret)

##

@dp.message_handler(commands=['search'])
async def process_search_command(message: types.Message):
    await message.reply(search(message))

##

error_message = text(
    "Жулик, играй по правилам"
)

@dp.message_handler()
async def echo_message(message: types.Message):
    await message.reply(error_message)
#    await bot.send_message(message.from_user.id, message.text)

'''
@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    message_text = text(emojize('Я не знаю, что с этим делать :astonished:'),
                        italic('\nЯ просто напомню,'), 'что есть',
                        code('команда'), '/help')
    await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)
'''

##

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
