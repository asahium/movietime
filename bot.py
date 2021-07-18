import logging
import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from kinodef import search, info, search_genre, new_in
from config import TOKEN
from kinodef import kino
import keyboards as kb
import random

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

start_message = text(
    "Привет 👋",
    "На связи бот @movieproject_bot! Как я могу тебе помочь?",
    "Например для поиска фильма введи /search + \
    \'часть названия фильма\'",
    "Для справки /help",
    sep="\n")


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(start_message, reply_markup=kb.markup_start)

help_message = text(
    "Это бот советчик по фильмам",
    "Доступные команды:\n",
    "/start - приветствие",
    "/search + \'часть названия фильма\' - поиск фильма",
    "/secret - нажми на меня",
    sep="\n")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)


@dp.message_handler(commands=['secret'])
async def process_command_1(message: types.Message):
    await message.reply("Хмм, интересно...", reply_markup=kb.inline_kb1)

error_message = text(
    "Жулик, играй по правилам")

new_message = text(
    'Главные новинки кино и сериалов только для тебя 🐣 \nЕсли соберёшься в кино - не забудь маску')

advice_message = text(
    'Отлично 🍿 \nЯ выберу для тебя что-нибудь из топа. Какой жанр тебе интересен?')


@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text == '🥧 Посоветуй фильм':
        await message.reply(advice_message, reply_markup=kb.markup2)

    elif message.text == '🍯 Комедия':
        await message.reply(search_genre('комедия'))

    elif message.text == '🐝 Фантастика':
        await message.reply(search_genre('фантастика'))

    elif message.text == '🧺 Драма':
        await message.reply(search_genre('драма'))

    elif message.text == '🍡 Боевик':
        await message.reply(search_genre('боевик'))

    elif message.text == 'Назад':
        await message.reply('Хорошо. Чего желаете?', reply_markup=kb.markup_start)

    elif message.text == '🌷 Случайный фильм':
        num = random.randint(1, 5000)
        ans = info(num)
        await message.reply('Сейчас сгенерирую для тебя что-нибудь интересное 🌺')
        await asyncio.sleep(2)
        await message.reply(ans, reply=False)

    elif message.text == '🌾 Что новенького?':
        await message.reply(new_message)
        await asyncio.sleep(2)
        await message.reply(new_in(), reply=False)

    elif message.text[:7] == '/search':
        await message.reply(search(message.text[7:]))

    else:
        await message.reply(error_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
