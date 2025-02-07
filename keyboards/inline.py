from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton

def dif_choice():

    kb = InlineKeyboardBuilder()
    kb.button(text='1.Easy(Легкий)',callback_data=f'easy')
    kb.button(text='2.Medium(Средний)',callback_data=f'medium')
    kb.button(text='3.Hard(Сложный)',callback_data=f'hard')

    kb.adjust(3)

    return kb.as_markup()

def found_kb(is_from=False):
    kb = InlineKeyboardBuilder()
    kb.button(text="✅ Found", callback_data="yes")
    kb.button(text="❌ Not Found", callback_data="no")
    kb.button(text="🔄 New Word", callback_data="new_word")

    kb.adjust(3)

    return kb.as_markup()