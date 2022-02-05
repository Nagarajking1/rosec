import os

from pyrogram import Client

API_ID = os.environ.get("7678244", None)
API_HASH = os.environ.get("e23d94ebe8749ebacabf19d597e0d94f", None)
TOKEN = os.environ.get("1955521660:AAGpUTiMawjm2FGAGLYOp-_bHWj8ZMZbrHc", None)

SHIZUKA = Client(":memory:", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
