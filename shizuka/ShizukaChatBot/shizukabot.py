import asyncio
import re

import aiohttp
import emoji
import requests
from coffeehouse.exception import CoffeeHouseError as CFError
from gpytranslate import Translator
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from shizuka import SHIZUKA

url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

translator = Translator()
BOT_ID = 1699240021


def extract_emojis(s):
    return "".join(c for c in s if c in emoji.UNICODE_EMOJI)


en_chats = []


@SHIZUKA.on_message(
    filters.text & filters.reply & ~filters.bot & ~filters.via_bot
    & ~filters.forwarded,
    group=2,
)
async def lycia(client, message):
    if message.reply_to_message.from_user.id != BOT_ID:
        message.continue_propagation()
    msg = message.text
    chat_id = message.chat.id
    hello = message.from_user.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    if chat_id in en_chats:
        onik = msg
        querystring = {
            "bid": "161901",
            "key": "Sgv5QAk5wEbhqYn0",
            "uid": hello,
            "msg": {test},
        }
        headers = {
            "x-rapidapi-key":
            "cf9e67ea99mshecc7e1ddb8e93d1p1b9e04jsn3f1bb9103c3f",
            "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        }
        response = requests.request("GET",
                                    url,
                                    headers=headers,
                                    params=querystring)
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace("<\/a>", "</a>")
        saini = result
        try:
            await SHIZUKA.send_chat_action(message.chat.id, "typing")
            await message.reply_text(saini)
        except CFError as e:
            print(e)
    else:
        u = msg.split()
        emj = extract_emojis(msg)
        msg = msg.replace(emj, "")
        if ([(k) for k in u if k.startswith("@")]
                and [(k) for k in u if k.startswith("#")]
                and [(k) for k in u if k.startswith("/")]
                and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []):

            h = " ".join(filter(lambda x: x[0] != "@", u))
            km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
            tm = km.split()
            jm = " ".join(filter(lambda x: x[0] != "#", tm))
            hm = jm.split()
            rm = " ".join(filter(lambda x: x[0] != "/", hm))
        elif [(k) for k in u if k.startswith("@")]:

            rm = " ".join(filter(lambda x: x[0] != "@", u))
        elif [(k) for k in u if k.startswith("#")]:
            rm = " ".join(filter(lambda x: x[0] != "#", u))
        elif [(k) for k in u if k.startswith("/")]:
            rm = " ".join(filter(lambda x: x[0] != "/", u))
        elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
            rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
        else:
            rm = msg
            lan = await translator.detect(rm)
        onik = rm
        if not "en" in lan and not lan == "":
            onik = translator.translate(onik, targetlang="en")

        querystring = {
            "bid": "161901",
            "key": "Sgv5QAk5wEbhqYn0",
            "uid": hello,
            "msg": {onik},
        }
        headers = {
            "x-rapidapi-key":
            "7c5d3fbeb6msh99d2dd0de3e3ef8p1d96b4jsnf7b3837c87a3",
            "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
        }
        response = requests.request("GET",
                                    url,
                                    headers=headers,
                                    params=querystring)
        result = response.text
        result = result.replace('{"cnt":"', "")
        result = result.replace('"}', "")
        result = result.replace("<a href=\\", "<a href =")
        result = result.replace("<\/a>", "</a>")
        saini = result
        if not "en" in lan and not lan == "":
            pro = translator.translate(saini, lang_tgt=lan[0])
        try:
            await SHIZUKA.send_chat_action(message.chat.id, "typing")
            await message.reply_text(saini)
        except CFError as e:
            print(e)


@SHIZUKA.on_message(filters.text & filters.private & ~filters.reply
                    & ~filters.bot)
async def chankit(client, message):
    msg = message.text
    hello = message.from_user.id
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if ([(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        lan = await translator.detect(rm)
    onik = rm
    if not "en" in lan and not lan == "":
        onik = translator.translate(onik, targetlang="en")

    querystring = {
        "bid": "161901",
        "key": "Sgv5QAk5wEbhqYn0",
        "uid": hello,
        "msg": {onik},
    }
    headers = {
        "x-rapidapi-key": "7c5d3fbeb6msh99d2dd0de3e3ef8p1d96b4jsnf7b3837c87a3",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace("<\/a>", "</a>")
    saini = result
    if not "en" in lan and not lan == "":
        saini = translator.translate(saini, targetlang=lan[0])
    try:
        await SHIZUKA.send_chat_action(message.chat.id, "typing")
        await message.reply_text(saini)
    except CFError as e:
        print(e)


@SHIZUKA.on_message(
    filters.regex("Lycia|lycia|SHIZUKA|shizuka||Shizuka")
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.forwarded
    & ~filters.reply
    & ~filters.channel)
async def chankit(client, message):
    msg = message.text
    if msg.startswith("/") or msg.startswith("@"):
        message.continue_propagation()
    u = msg.split()
    emj = extract_emojis(msg)
    msg = msg.replace(emj, "")
    if ([(k) for k in u if k.startswith("@")]
            and [(k) for k in u if k.startswith("#")]
            and [(k) for k in u if k.startswith("/")]
            and re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []):

        h = " ".join(filter(lambda x: x[0] != "@", u))
        km = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", h)
        tm = km.split()
        jm = " ".join(filter(lambda x: x[0] != "#", tm))
        hm = jm.split()
        rm = " ".join(filter(lambda x: x[0] != "/", hm))
    elif [(k) for k in u if k.startswith("@")]:

        rm = " ".join(filter(lambda x: x[0] != "@", u))
    elif [(k) for k in u if k.startswith("#")]:
        rm = " ".join(filter(lambda x: x[0] != "#", u))
    elif [(k) for k in u if k.startswith("/")]:
        rm = " ".join(filter(lambda x: x[0] != "/", u))
    elif re.findall(r"\[([^]]+)]\(\s*([^)]+)\s*\)", msg) != []:
        rm = re.sub(r"\[([^]]+)]\(\s*([^)]+)\s*\)", r"", msg)
    else:
        rm = msg
        lan = translator.detect(rm)
    onik = rm
    if not "en" in lan and not lan == "":
        onik = await translator.translate(onik, targetlang="en")
    querystring = {
        "bid": "161901",
        "key": "Sgv5QAk5wEbhqYn0",
        "uid": hello,
        "msg": {onik},
    }
    headers = {
        "x-rapidapi-key": "7c5d3fbeb6msh99d2dd0de3e3ef8p1d96b4jsnf7b3837c87a3",
        "x-rapidapi-host": "acobot-brainshop-ai-v1.p.rapidapi.com",
    }
    response = requests.request("GET",
                                url,
                                headers=headers,
                                params=querystring)
    result = response.text
    result = result.replace('{"cnt":"', "")
    result = result.replace('"}', "")
    result = result.replace("<a href=\\", "<a href =")
    result = result.replace("<\/a>", "</a>")
    pro = result
    if not "en" in lan and not lan == "":
        saini = translator.translate(saini, targetlang=lan[0])
    try:
        await SHIZUKA.send_chat_action(message.chat.id, "typing")
        await message.reply_text(saini)
    except CFError as e:
        print(e)
