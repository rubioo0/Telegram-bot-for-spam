import contextlib
import asyncio
from aiogram.types import ChatJoinRequest, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, F
import logging

BOT_TOKEN = '6627215613:AAFrXbyBH4rEsjXs9K13RCrlLYjgc0M4T4Y'
CHANNEL_ID = -1002077231905
ADMIN_ID = 5376793030 


async def approve_request(chat_join: ChatJoinRequest, bot: Bot):
    msg = f'‼️Чтобы увидеть продолжение — Подпишитесь на каналы ниже ‼️\r\n\r\n' \
          f'ОБЯЗАТЕЛЬНО 🔞'

    # Create an inline keyboard with three buttons, each with callback_data for functionality
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Канал с треш новостями🔞", url="https://telega.news/go/xxlOunL58EOwAYX4R8vRQw")],
        [InlineKeyboardButton(text="Лучшие треш новости🔞", url="https://telega.news/go/PD97cLFjTkaCnjp3ixBWoQ")],
        [InlineKeyboardButton(text="ОСТАЛЬНОЙ ТРЕШ 😳", url="https://telega.news/go/kUZ6OB2ckiHXF54exGNgw")]
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

