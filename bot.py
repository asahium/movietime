import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from kinodef import search, info
from config import TOKEN
from kinodef import kinopoisk
import keyboards as kb
import random

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

##

start_message = text(
    "Привет 👋",
    "На связи бот @movieproject_bot! Как я могу тебе помочь?",
    "Для справки /help",
    sep="\n"
)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply(start_message, reply_markup=kb.markup_start)

##

help_message = text(
    "Это бот советчик по фильмам",
    "Доступные команды:\n",
    "/start - приветствие",
    "/search + \'часть названия фильма\' - поиск фильма",
    "/search_full + \'название фильма\' - инфо о фильме по точному названию",
    "/secret - нажми на меня",
    sep="\n"
)

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(help_message)

##

@dp.message_handler(commands=['secret'])
async def process_command_1(message: types.Message):
    await message.reply("Хмм, интересно...", reply_markup=kb.inline_kb1)

##

@dp.message_handler(commands=['search'])
async def process_search_command(message: types.Message):
    await message.reply(search(message))

##

@dp.message_handler(commands=['search_full'])
async def process_fullsearch_command(message: types.Message):
    await message.reply(search(message))

##

error_message = text(
    "Жулик, играй по правилам(ну или я просто не сделал эту кнопку пока)"
)

@dp.message_handler()
async def echo_message(message: types.Message):
    if message.text == '🥧 Посоветуй фильм':

        await message.reply('Выбери жанр', reply_markup=kb.markup_advice)

    elif message.text == '🍯 Комедия':
        await message.reply('Ничего, сиди дома')

    elif message.text == '🧃 Мультфильм':
        await message.reply('Ничего, сиди дома')

    elif message.text == '🐝 Фантастика':
        await message.reply('Ничего, сиди дома')

    elif message.text == '🧺 Драма':
        await message.reply('Ничего, сиди дома')

    elif message.text == '🍡 Боевик':
        await message.reply('Ничего, сиди дома')

    elif message.text == 'Назад':
        await message.reply('Хорошо. Чего желаете?', reply_markup=kb.markup_start)

    elif message.text == '🌷 Случайный фильм':
        num = random.randint(1, 5000)
        ans = info(num)
        t = kinopoisk.get_film(num)
        inline_btn_2 = InlineKeyboardButton(text='Ссылка на фильм', url=t.kp_url)
        inline_kb2 = InlineKeyboardMarkup().add(inline_btn_2)
        await message.reply(ans, reply_markup=inline_kb2)

    elif message.text == '🌾 Что сейчас в кино?':
        await message.reply('Ничего, сиди дома')

    else:
        await message.reply(error_message)

##

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
