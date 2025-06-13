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
📄 requirements.txt
txt
Copy code
aiogram==3.4.1
python-dotenv
📄 render.yaml
yaml
Copy code
services:
  - type: web
    name: auto-delete-bot
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python main.py
    envVars:
      - key: BOT_TOKEN
        value: your_bot_token_here
      - key: DELETE_DELAY
        value: 10
📄 README.md
markdown
Copy code
# Telegram Auto Delete Bot

A simple Telegram bot that deletes messages automatically after a few seconds.

## 🛠 Deploy on Render

1. Fork or download this repo.
2. Go to [Render.com](https://render.com/) → New → Web Service.
3. Connect your GitHub repo.
4. Set environment variable:
   - `BOT_TOKEN` = Your bot token from BotFather
   - `DELETE_DELAY` = Time (in seconds) to auto delete
5. Deploy. Done!

## 💡 Features

- Deletes every message in a chat after a fixed delay.
- Lightweight, runs on free tier.
📦 Download ZIP
I'll now prepare the .zip file for you. Give me a moment…

✅ Your Telegram Auto Delete Bot project with Render support is ready!

📦 Click here to download the ZIP file

Let me know if you want Koyeb support or any custom changes (like delete for specific users, command toggles, etc.). 











Tools



ChatGPT can make mistakes. Check important info. See Cookie Preferences.
