import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, User, Message

Client = Client(
    "Service message remover",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_BUTTON=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Support Group", url="https://t.me/pyrogrammers"),
                     InlineKeyboardButton("Updats Channel", url="https://t.me/pocketfmhub")],
                    [InlineKeyboardButton("YouTube", url="https://youtube.com/channel/UC2anvk7MNeNzJ6B4c0SZepw")]
                ])

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, message):
    await message.reply_text(
        f""" Hii {message.from_user.mention} i am Anti spam bot i can remove Service Message, command and https links in groups.""", 
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    )
@Client.on_message(filters.regex("http") | filters.regex("t.me") | filters.regex("in") | filters.regex("youtu.be") | filters.regex("com") | filters.regex("https") | filters.regex("/" ) | filters.service)
async def delete(bot,message):
 await message.delete()

Client.run()
