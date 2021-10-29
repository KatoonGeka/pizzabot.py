from aiogram import Dispatcher, types
from create_bot import bot
from keyboard import kb_client
from database import sqlitedb

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, "Приятного аппетита", reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Бот не может вам ответить напишите ему: \n https://t.me/easy111_bot')

#@dp.message_handler(commands=['Режим_работы'])
async def work_command(message: types.message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 10-00 до 23-00, Сб-Вс с 11-00 до 20-00')

#@dp.message_handler(commands=['Локация'])
async def location_command(message: types.message):
    await bot.send_message(message.from_user.id, 'ул. Пушкина дом Колотушкина')

#@dp.message_handler(commands=['Меню'])
async def menu_command(message:types.Message):
    await sqlitedb.sql_read(message)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(work_command, commands=['Режим_работы'])
    dp.register_message_handler(location_command, commands=['Локация'])
    dp.register_message_handler(menu_command, commands=['Меню'])