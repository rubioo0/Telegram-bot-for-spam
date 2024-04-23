from aiogram import Bot
from aiogram.types import Message
import logging
import json
from core.keyboards.reply import reply_keyboard
from core.utils.dbconnect import Request

async def get_start(message: Message, bot: Bot, counter : str, request: Request):
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await bot.send_message(message.from_user.id, f'<b>Hi {message.from_user.first_name}. I am glad to see you!</b>')
    await message.answer(f'<s>Hi {message.from_user.first_name}. I am glad to see you!</s>')
    await message.reply(f'<tg-spoiler>Hi {message.from_user.first_name}. I am glad to see you!</tg-spoiler>')


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Excellent. You sent a photo. I will save it.')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')


async def get_hello(message: Message, bot:Bot):
    await message.answer(f'So Hi to you')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
