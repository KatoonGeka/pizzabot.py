from aiogram.types import ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Локация')
b3 = KeyboardButton('/Меню')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).insert(b3)
