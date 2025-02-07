from aiogram.utils.keyboard import ReplyKeyboardBuilder

def team_choice():
    kb = ReplyKeyboardBuilder()

    kb.button(text='ALPHA')
    kb.button(text='BETA')
    kb.button(text='END')
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)