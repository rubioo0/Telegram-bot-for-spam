from aiogram import Bot
from aiogram.types import BotCommand, bot_command_scope_default

async def set_commands(bot:Bot):
    commands = [
        BotCommand(
            command='start',
            description='Start of work'
        ),
        BotCommand(
            command='Hi',
            description="Help"
        ),
        BotCommand(
            command="Cancel",
            description="Reset"
        )
    ]

    await bot.set_my_commands(commands, bot_command_scope_default())