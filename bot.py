from pyrogram import Client, filters
from pyrogram.types import Message

API_ID=26742257
API_HASH=625a7410153e4222aa34b82b9cff2554
BOT_TOKEN = "8140339685:AAEtkGgjxUF32-2w7BCxsktmw67_OXxQZh0"  # From @BotFather
OWNER_ID = 7743703095  # Your Telegram user ID
TARGET_CHANNEL = -1002414767028  # Channel ID where files should be sent

app = Client("forward_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.private & filters.user(OWNER_ID))
async def forward_file(client: Client, message: Message):
    if message.media:
        try:
            await message.copy(chat_id=TARGET_CHANNEL)
            await message.reply_text("✅ File sent to channel without forward tag.")
        except Exception as e:
            await message.reply_text(f"❌ Error: {e}")
    else:
        await message.reply_text("❗ Please send a media file (video, photo, document, etc.)")


app.run()
