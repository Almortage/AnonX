import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup

from AnonXMusic import app
from random import  choice, randint

@app.on_message(filters.command(["صوره", "🕷", "صورهه", "صور"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,75)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار صوره لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )


@app.on_message(filters.command(["انميي", "انمي"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(3,153)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار انمي لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )


@app.on_message(filters.command(["متحركه. 🎬", "متحركه"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,926)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(message.chat.id,url,caption="💙 ¦ تـم اختيـار ملصق لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )

@app.on_message(filters.command(["تلاوات", "تلاوة"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(24,618)
    url = f"https://t.me/EIEI06/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار تلاوة قرآنيه لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )
    
@app.on_message(filters.command(["اقتباسات", "اقتباس"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(3,102)
    url = f"https://t.me/LoreBots9/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار اقتباس لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )

@app.on_message(filters.command(["هيدرا", "هيدرات"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,153)
    url = f"https://t.me/flflfldld/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار هيدرات لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )

@app.on_message(filters.command(["صور", "افاتار بنات"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,216)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار افاتار بنات لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )

@app.on_message(filters.command(["صور شباب", "افاتار شباب"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,148)
    url = f"https://t.me/vgbmm/{rl}"
    await client.send_photo(message.chat.id,url,caption="💙 ¦ تـم اختيـار افاتار شباب لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )

@app.on_message(filters.command(["سوره", "قران"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,82)
    url = f"https://t.me/opuml/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار ايـه قرآنيه لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )

@app.on_message(filters.command(["الشيخ", "النقشبندي", "نقشبندي"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,114)
    url = f"https://t.me/ggcnjj/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ نقشبندي لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )
    
@app.on_message(filters.command(["عبدالباسط", "عبدالباسط عبدالصمد"], "")
& filters.group
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(7,265)
    url = f"https://t.me/telawatnader/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ عبدالباسط لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )
    
@app.on_message(filters.command(["استوري", "استوريهات. 🥹"], "")
& filters.group 
& ~filters.private
)
async def ihd(client: Client, message: Message):
    rl = random.randint(2,148)
    url = f"https://t.me/yoipopl/{rl}"
    await client.send_audio(message.chat.id,url,caption="💚 ¦ تـم اختيـار استوري لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech")
                ],
            ]
        )
    )
