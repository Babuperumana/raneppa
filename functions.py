from config import bot
import os
from telebot import types


def set_keyboard(buttons):
    keyboard = types.ReplyKeyboardMarkup(
        row_width=2, resize_keyboard=True, one_time_keyboard=False
    )
    for elem in buttons:
        keyboard.row(elem)
    return keyboard


def send_doc(file_name, path, id, keyboard=None):
    bot.send_document(id, open(path + file_name, "rb"), reply_markup=keyboard)


def send_photo(file_name, path, id, keyboard=None, desc=None):
    bot.send_photo(id, open(path + file_name, "rb"), reply_markup=keyboard, caption=desc)


def send_text(message, id, parse=None, keyboard=None):
    bot.send_message(id, message, parse_mode=parse, reply_markup=keyboard)