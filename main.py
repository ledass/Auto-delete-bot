import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from os import getenv
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("BOT_TOKEN")
DELETE_DELAY = int(getenv("DELETE_DELAY", 10))  # default 10 seconds

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(msg: Message):
    sent = await msg.answer("I'm an auto-delete bot. I will delete this in {} seconds.".format(DELETE_DELAY))
    await asyncio.sleep(DELETE_DELAY)
    await msg.delete()
    await sent.delete()

@dp.message()
async def delete_everything(msg: Message):
    await asyncio.sleep(DELETE_DELAY)
    try:
        await msg.delete()
    except:
        pass  # message already deleted or can't be deleted

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
