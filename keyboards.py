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

text_button_hi_4 = text(
    '🍄 Быстрый поиск'
)

button_hi_1 = KeyboardButton(text_button_hi_1)
button_hi_2 = KeyboardButton('🌷 Фильм дня')
button_hi_3 = KeyboardButton(text_button_hi_3)
button_hi_4 = KeyboardButton(text_button_hi_4)

markup_start = ReplyKeyboardMarkup().add(button_hi_1).add(button_hi_2).add(button_hi_3).add(button_hi_4)






secret.add(InlineKeyboardButton('Тык', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLxb0XwjhqM_RLETkiOkUZrEE8K-fP3V-p&index=3'))
