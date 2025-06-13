import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("BOT_TOKEN")
DELETE_DELAY = int(os.getenv("DELETE_DELAY", 10))

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    sent = await message.answer("Hi! I will auto-delete messages in {} seconds.".format(DELETE_DELAY))
    await asyncio.sleep(DELETE_DELAY)
    await bot.delete_message(message.chat.id, message.message_id)
    await bot.delete_message(sent.chat.id, sent.message_id)

@dp.message_handler()
async def delete_all(message: types.Message):
    await asyncio.sleep(DELETE_DELAY)
    try:
        await bot.delete_message(message.chat.id, message.message_id)
    except:
        pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
                     
