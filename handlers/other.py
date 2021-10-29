from aiogram import Bot, Dispatcher, types
API_TOKEN = '2060189311:AAFo-L3GBcDw3WNLn1wKlkBUcn3lGPJDMjs'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


#@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id,message.text)

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(echo)
