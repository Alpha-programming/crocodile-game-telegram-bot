from aiogram.fsm.state import State, StatesGroup

class FoundState(StatesGroup):
    text = State()