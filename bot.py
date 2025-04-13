import os
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import Message
import threading

API_ID=26742257
API_HASH="625a7410153e4222aa34b82b9cff2554"
BOT_TOKEN = "8140339685:AAEtkGgjxUF32-2w7BCxsktmw67_OXxQZh0"  # From @BotFather
OWNER_ID = 7743703095  # Your Telegram user ID
TARGET_CHANNEL = -1002414767028  # Channel ID where files should be sent

# Start Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is running!"

# Start Pyrogram bot in a separate thread
pyro_app = Client("forward_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@pyro_app.on_message(filters.private & filters.user(OWNER_ID))
async def forward_file(client: Client, message: Message):
    if message.media:
        try:
            await message.copy(chat_id=TARGET_CHANNEL)
            await message.reply_text("✅ File sent to channel without forward tag.")
        except Exception as e:
            await message.reply_text(f"❌ Error: {e}")
    else:
        await message.reply_text("❗ Please send a media file.")

def run_pyrogram():
    pyro_app.run()

if __name__ == "__main__":
    threading.Thread(target=run_pyrogram).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
