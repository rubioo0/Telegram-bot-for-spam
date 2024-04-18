import sqlite3
import contextlib
import asyncio
from aiogram.types import ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, F
import logging

BOT_TOKEN = '6627215613:AAFrXbyBH4rEsjXs9K13RCrlLYjgc0M4T4Y'
CHANNEL_ID = -1002077231905
ADMIN_ID = 5376793030 




class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM 'users' WHERE 'user_id' = ?", (user_id,)).fetchmany(1)
            return bool(len(result))
        
    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        
    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `active` = ? WHERE `user_id` = ?", (active, user_id,))
        
    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT `user_id`, `active` FROM 'users'").fetchall()

async def approve_request(chat_join: ChatJoinRequest, bot: Bot):
    db = Database('database.db')
    if not db.user_exists(chat_join.from_user.id):
        db.add_user(chat_join.from_user.id)
    msg = f'‼️Чтобы увидеть продолжение — Подпишитесь на каналы ниже ‼️\r\n\r\n' \
          f'ОБЯЗАТЕЛЬНО 🔞'

    # Create an inline keyboard with three buttons, each with callback_data for functionality
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Канал с треш новостями🔞", url="t.me/prodiiich_bot")],
        [InlineKeyboardButton(text="Лучшие треш новости🔞", url="https://t.me/+pPUILzAhnz8yYzYy")],
        [InlineKeyboardButton(text="ОСТАЛЬНОЙ ТРЕШ 😳", url="https://t.me/+1SxGSLJe8egwOWQy")],
        [InlineKeyboardButton(text="ОСТАЛЬНОЙ ТРЕШ 😳", url="https://t.me/+zmvlMS3iEqkwZWUy")]

    ])

    await bot.send_message(chat_id=chat_join.from_user.id, text=msg, reply_markup=keyboard)

async def start():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                                     "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )

    bot: Bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.chat_join_request.register(approve_request, F.chat.id == CHANNEL_ID)



    try:
        await dp.start_polling(bot)  # Remove allowed_updates parameter
    except Exception as ex:
        logging.error(f'[Exception] - {ex}', exc_info=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(start())
