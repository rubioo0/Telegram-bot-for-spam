from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,  # Ensures the keyboard replaces the user's default keyboard
    one_time_keyboard=True,  # Hides the keyboard after the user interacts with it (optional)
    keyboard=[
        [KeyboardButton(text="ROW1.Button1"), KeyboardButton(text="ROW1.Button2")],
        [KeyboardButton(text="ROW1.Button3"), KeyboardButton(text="ROW1.Button4")],
        [KeyboardButton(text="ROW3.Button5"), KeyboardButton(text="ROW3.Button7")],
        [KeyboardButton(text="ROW4.Button5"), KeyboardButton(text="ROW4.Button7")],
    ]
)
