import asyncio
import time
from telegram import Bot
from flask import Flask
from threading import Thread

TOKEN = "7985151266:AAHQR0KVL_3Fm9vdgJsVm0Gw83ZUh6yEYFU"
CHAT_ID = 1094467692

bot = Bot(token=TOKEN)

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()

async def send_msg():
    await bot.send_message(chat_id=CHAT_ID, text="Paani pee le 💧")

while True:
    asyncio.run(send_msg())
    time.sleep(7200)