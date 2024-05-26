import os
import json
import asyncio
from aiogram import Bot, Dispatcher, types
from datetime import datetime
#from aiogram.types import ParseMode

from dotenv import load_dotenv

import logging
from aiogram.filters.command import Command

from handlers import bot_messages, user_commands, addnotify, notifylist
from middleware import access

import keyboards

load_dotenv() 
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID'))

async def main():

    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)
    # Объект бота
    bot = Bot(token=BOT_TOKEN,
                 #parse_mode=ParseMode.HTML
                 )
    dp = Dispatcher()

    # Порядокк важен!
    dp.include_routers(
        user_commands.router,
        bot_messages.router,
        addnotify.router,
        notifylist.router    
    )

    dp.message.middleware(
            access.AccessMiddleware()
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())