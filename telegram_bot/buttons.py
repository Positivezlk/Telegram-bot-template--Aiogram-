from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

# Кнопки для Первой функции
button_func_1 = InlineKeyboardBuilder()
button_func_1.add(types.InlineKeyboardButton(text="Функция 1", callback_data='function_1'))
