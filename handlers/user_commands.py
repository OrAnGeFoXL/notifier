from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage


import os

from keyboards import reply

router=Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
       
    await message.answer(f"Привет, {message.from_user.full_name}!")
    
    #TODO Разместить приветственное сообщение

