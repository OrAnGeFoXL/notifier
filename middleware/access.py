import os

from typing import Any, Callable, Dict, Awaitable

from aiogram.types import Message
from aiogram.types import TelegramObject

from aiogram.dispatcher.middlewares.base import BaseMiddleware

from dotenv import load_dotenv

from bot import ADMIN_ID

allowed_user_ids =[ADMIN_ID]+[
                     123456789,
                     987654321,
                     984304271 
                     ]
print(allowed_user_ids)

class AccessMiddleware(BaseMiddleware):
    '''Блокирует сообщения от незарегистрированных пользователей'''

    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict], Awaitable[Any]],
            event: TelegramObject,
            data: dict,
    ) -> Any:
        #получаем id пользователя
        user_id = data['event_from_user'].id

        if user_id not in allowed_user_ids:
            await event.answer("Доступ запрещен для не зарегистрированных пользователей \n Обратитесь к администратору", show_alert=True)
            return None
        return await handler(event, data)
