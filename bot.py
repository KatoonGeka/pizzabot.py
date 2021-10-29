import logging

from aiogram import executor
from create_bot import dp
from database import sqlitedb

def on_startup():
    print('bot online')
    sqlitedb.sql_start()


logging.basicConfig(level=logging.INFO)

from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup())
