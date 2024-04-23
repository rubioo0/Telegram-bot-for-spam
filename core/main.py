from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from core.handlers.basic import get_start, get_photo, get_hello
from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_fake_contact, get_true_contact
import asyncio
import logging
from core.settings import settings
from aiogram import F  
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.filters import Command, CommandStart
from core.middlewares.dbmiddleware import DbSession
import asyncpg


async def start_bot(bot: Bot):
    # await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='The bot is started !')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='The bot is stopped !')


async def create_pool():
    return await asyncpg.create_pool(
        user='postgres',
        password='Starapps123',
        database='users',
        host='127.0.0.1',
        port=5432,
        command_timeout=60
    )



async def start():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                                "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    pool_connect = await create_pool()
    storage = RedisStorage.from_url('redis://localhost:6379/0') 
    dp = Dispatcher(storage=storage)
    dp.update.middleware.register(DbSession(pool_connect)) 
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    # dp.message.register(get_photo, F(content_types=[ContentType.PHOTO]))
    dp.message.register(get_photo, F.photo)
    dp.message.register(get_hello, F.text == 'Hi')
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_fake_contact, F.contact)
    dp.message.register(get_start, Command(commands=['start', 'run']))
    # dp.message.register(get_start, CommandStart)  # Uncomment if needed

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
