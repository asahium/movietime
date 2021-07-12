from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import text


text_button_hi_1 = text(
    '🥧 Посоветуй фильм',
    'рандомный фильм из топа',
    sep='\n'
)

text_button_hi_3 = text(
    '🌾 Что сейчас в кино?',
    'выводит киноафишу',
    sep='\n'
)

text_button_hi_4 = text(
    '🍄 Быстрый поиск',
    'поиск по названию',
    sep='\n'
)

button_hi_1 = KeyboardButton(text_button_hi_1)
button_hi_2 = KeyboardButton('🌷 Фильм дня')
button_hi_3 = KeyboardButton(text_button_hi_3)
button_hi_4 = KeyboardButton(text_button_hi_4)

markup_start = ReplyKeyboardMarkup().add(button_hi_1).add(button_hi_2).add(button_hi_3).add(button_hi_4)
