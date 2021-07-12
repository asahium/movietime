from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import text


text_button_hi_1 = text(
    '🥧 Посоветуй фильм'
)

text_button_hi_3 = text(
    '🌾 Что сейчас в кино?'
)

button_hi_1 = KeyboardButton(text_button_hi_1)
button_hi_2 = KeyboardButton('🌷 Фильм дня')
button_hi_3 = KeyboardButton(text_button_hi_3)

markup_start = ReplyKeyboardMarkup().add(button_hi_1).add(button_hi_2).add(button_hi_3)




button_secret = KeyboardButton('Тык', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLxb0XwjhqM_RLETkiOkUZrEE8K-fP3V-p&index=3')

secret = ReplyKeyboardMarkup().add(button_secret)
