import os
from pyrogram import Client, filters

TOKEN = os.getenv("BOT_TOKEN")

app = Client("peaks_counter", bot_token=TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("أهلاً بك! هذا بوت Peaks Counter.")

app.run()
