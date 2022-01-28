from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from shizuka import SHIZUKA

SHIZUKA_START = """
I am PHOENIX 『@PHOENIX_CHAT_TAMIL』, An Intelligent ChatBot.[⠀](https://telegra.ph/file/6502c7fa93135c478e5a2.jpg)
"""


@SHIZUKA.on_message(
    filters.command(["start"], prefixes=["/", "!"]) & ~filters.edited)
async def info(client, message):
    buttons = [
        [
            InlineKeyboardButton(text="Go inline",
                                 switch_inline_query_current_chat="shizuka "),
        ],
        [
            InlineKeyboardButton(
                "OWNER",
                url="https://t.me/Jaihindupuramking"),
            InlineKeyboardButton("Maintained by",
                                 url="https://t.me/PHOENIX_CHAT_TAMIL"),
        ],
    ]
    await SHIZUKA.send_message(
        chat_id=message.chat.id,
        text=SHIZUKA_START,
        reply_markup=InlineKeyboardMarkup(buttons),
    )
