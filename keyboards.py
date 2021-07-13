from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import text


button_hi_1 = KeyboardButton('🥧 Посоветуй фильм')
button_hi_2 = KeyboardButton('🌷 Случайный фильм')
button_hi_3 = KeyboardButton('🌾 Что сейчас в кино?')

button_hi_4 = KeyboardButton('🍯 Комедия')
button_hi_5 = KeyboardButton('🧃 Мультфильм')
button_hi_6 = KeyboardButton('🐝 Фантастика')
button_hi_7 = KeyboardButton('🧺 Драма')
button_hi_8 = KeyboardButton('🍡 Боевик')
button_hi_9 = KeyboardButton('Назад')

markup_start = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi_1).add(button_hi_2).add(button_hi_3)

markup_advice = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi_4).add(button_hi_5).add(button_hi_6).add(button_hi_7).add(button_hi_8).add(button_hi_9)

inline_btn_1 = InlineKeyboardButton(text='Что делает эта кнопка?', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=PLxb0XwjhqM_RLETkiOkUZrEE8K-fP3V-p&index=3')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
