from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

from utils.states import AddNotify

from keyboards import reply

from libs.data import write_notify_to_sqlite

from datetime import datetime

router = Router()


message_1="Связать напоминание с целью:"


@router.message(Command("addnotify"))
async def description(message: Message, state: FSMContext):
    
    await state.set_state(AddNotify.text)
    await message.answer("Введите текст напоминания:")


@router.message(AddNotify.text)
async def set_time(message: Message, state: FSMContext):

    if len(message.text) > 60:
        await message.answer("Слишком длинное сообщение. Введите не более 60 символов.")
    else:
        await state.update_data(text=message.text)
        await state.set_state(AddNotify.time)
        await message.answer("Введи время напоминания в формате: 00:00")


@router.message(AddNotify.date)
async def add_date(message: Message, state: FSMContext):

    pass


@router.message(AddNotify.time)
async def add_time(message: Message, state: FSMContext):

    try:
        datetime.strptime(message.text, '%H:%M')
    except ValueError:
        await message.answer("Неверный формат времени. Введите время в формате: hh:mm")
        return

    await state.update_data(time=message.text)
    await state.set_state(AddNotify.repeat)
    await message.answer("Требуется повторять напоминание?",
                reply_markup=reply.yes_no_kb(),
                one_time_keyboard=True
                )
    data = await state.get_data()
    text = data.get("time")


@router.message(AddNotify.repeat)
async def add_amount(message: Message, state: FSMContext):

    await state.update_data(repeat=message.text)
    if message.text == "Да":
        await state.set_state(AddNotify.repeat_frq)
        await message.answer("Как часто требуется повторять напоминание?",
                reply_markup=reply.repeat_frq_kb(),
                one_time_keyboard=True
                )
    elif message.text == "Нет":
        await state.update_data(repeat_frq="Никогда")
        await state.set_state(AddNotify.task)
        await message.answer(message_1,
                reply_markup=reply.yes_no_kb(),
                one_time_keyboard=True
                )
    else:
        await message.answer("Неверное значение.\nВведите Да или Нет")


@router.message(AddNotify.repeat_frq)
async def add_frq(message: Message, state: FSMContext):
    
    await state.update_data(repeat_frq=message.text, reply_markup=reply.yes_no_kb())
    await state.set_state(AddNotify.task)

    await message.answer(message_1,
            reply_markup=reply.yes_no_kb(),
            one_time_keyboard=True
            )


async def approve_fnc(message: Message, state: FSMContext):

    await state.update_data(task=message.text)
       
    data = await state.get_data()
    text = data.get("text")
    time = data.get("time")
    repeat = data.get("repeat")
    repeat_frq = data.get("repeat_frq")
    task = data.get("task")
       
    await message.answer(
        f"Время: <b>{time}</b>\nТекст: <b>{text}</b>\nПовторять: <b>{repeat}</b> \nЧастота: <b>{repeat_frq}</b> \nЗадача: <b>{task}</b>",
          parse_mode="HTML")
    await message.answer("Все верно?", reply_markup=reply.yes_no_kb())


@router.message(AddNotify.task) 
async def add_frq(message: Message, state: FSMContext):

    if message.text == "Да":
        await state.update_data(task=message.text)
        await state.set_state(AddNotify.approve)
        await message.answer("Выберите задачу", reply_markup=reply.yes_no_kb())

    elif message.text == "Нет":
        await state.update_data(task=message.text)
        await state.set_state(AddNotify.approve)
        await approve_fnc(message, state)
    else:
        await message.answer("Неверное значение.\nВведите Да или Нет") 
    

@router.message(AddNotify.approve, F.text == "Да")
async def approve(message: Message, state: FSMContext):
    await write_notify_to_sqlite(state, message)
    print(message)
    await state.clear()
    await message.answer("✅ Напоминание создано \nВведите /addnotify чтобы создать новое напоминание", reply_markup=ReplyKeyboardRemove())


@router.message(AddNotify.approve, F.text == "Нет")
async def cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("🚫 Напоминание отменено \nВведите /addnotify чтобы создать новое напоминание", reply_markup=ReplyKeyboardRemove())





