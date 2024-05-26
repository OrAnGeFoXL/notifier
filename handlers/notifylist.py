from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from libs.data import get_notifications

router=Router()

@router.message(Command("notifylist"))
async def send_notifylist(message: Message):
    
    notifications = await get_notifications(message.from_user.id)

    if notifications:
        notification_list = "\n".join([
            f"📝 Text: {notification[0]}\n"
            f"🕒 Time: {notification[1]}\n"
            f"🔁 Repeat: {notification[2]}\n"
            f"🔁⏳ Repeat Frequency: {notification[3]}\n"
            f"🏁 Task: {notification[4]}\n"
            for notification in notifications
        ])
        await message.answer(
            f"Here is the list of notifications for user_id {message.from_user.id}:\n\n{notification_list}",
            #parse_mode="MarkdownV2",
        )
    else:
        await message.answer(
            f"No notifications found for user_id {message.from_user.id}.",
            #parse_mode="MarkdownV2",
        )

