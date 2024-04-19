import logging
from aiogram import Bot, Dispatcher, executor, types
from db import Database

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6735109800:AAHflICtWdXhEBk0e7DttawAkvwHKpS_p8s")
dp = Dispatcher(bot)
db = Database('database.db')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, "Hi")

@dp.message_handler(commands=['clearallusers'])
async def clear_all_users(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 5376793030:
            db.clear_all_users()
            await bot.send_message(message.from_user.id, "All user information cleared from the database.")

@dp.message_handler(commands=['sendall'])
async def sendall(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 5376793030:
            text = message.text[9:]

            if not text:
                await bot.send_message(message.from_user.id, "Please provide a message to send to all users.")
                return

            users = db.get_users()

            for row in users:
                try:
                    await bot.send_message(row[0], text)
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                except Exception as e:
                    logging.error(f"Error sending message to user {row[0]}: {e}")
                    db.set_active(row[0], 0)

            await bot.send_message(message.from_user.id, "Message sent to all users.")

@dp.message_handler(commands=['sendmediaall'])
async def send_media_all(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == 5376793030:
            media = None

            if message.reply_to_message and message.reply_to_message.photo:
                media = [types.InputMediaPhoto(media=message.reply_to_message.photo[-1].file_id)]
            elif message.reply_to_message and message.reply_to_message.video:
                media = [types.InputMediaVideo(media=message.reply_to_message.video.file_id)]
            else:
                await bot.send_message(message.from_user.id, "Please reply to a photo or video to send it to all users.")
                return

            users = db.get_users()

            for row in users:
                try:
                    if media:
                        await bot.send_media_group(row[0], media)
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                except Exception as e:
                    logging.error(f"Error sending media to user {row[0]}: {e}")
                    db.set_active(row[0], 0)

            await bot.send_message(message.from_user.id, "Media sent to all users.")

@dp.chat_member_handler()
async def welcome_new_member(message: types.ChatMemberUpdated):
    # Check if the user is joining the channel
    if message.new_chat_member and message.new_chat_member.status == 'member':
        # Send a greeting message
        await bot.send_message(message.chat.id, f"Welcome {message.new_chat_member.user.first_name}!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
