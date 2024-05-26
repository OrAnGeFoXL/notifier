from aiogram.fsm.state import StatesGroup, State

class Waste(StatesGroup):
    category = State()
    amount = State()
    note = State()
    approve = State()
    cancel = State()


class AddNotify(StatesGroup):
    text = State()
    date = State()
    time = State()
    repeat = State()
    repeat_frq = State()
    task = State()

    approve = State()
    cancel = State()