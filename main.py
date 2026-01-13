from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot("8346433002:AAHhND4SrSpPSvlWrTf2HcLU6hA3XgxJPBs")
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Open website", web_app=WebAppInfo(url="https://itproger.com")))
    await message.answer("Hello my friend", reply_markup=markup)

executor.start_polling(dp)