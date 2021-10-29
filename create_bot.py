from aiogram import Bot, Dispatcher

from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()

API_TOKEN = '2060189311:AAFo-L3GBcDw3WNLn1wKlkBUcn3lGPJDMjs'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)