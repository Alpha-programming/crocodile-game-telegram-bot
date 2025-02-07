from aiogram import Router
from aiogram.types import  Message
from aiogram.filters.command import CommandStart,Command
from keyboards.reply import team_choice
from database.sql import save_user_to_db
router = Router()

@router.message(CommandStart())
async def start(message: Message):
    user = message.from_user

    save_user_to_db(
        user_id=user.id,
        first_name=user.first_name,
        last_name=user.last_name or "None",
        username=user.username or "None",
        language_code=user.language_code or "Unknown",
        is_bot=user.is_bot
    )

    await message.answer('''Welcome to the crocodile game!
Choose your team below.''',
                         reply_markup=team_choice())


@router.message(Command(commands='info'))
async def info(message: Message):
    await message.answer('''ENGLISH
One player explains a word without saying it, while others try to guess it.
The explanation can be verbal or through gestures (if playing in person).
The first to guess correctly wins the round!

RUSSIAN
Один игрок объясняет слово, не называя его, а другие пытаются угадать.
Объяснять можно словами или жестами.
Тот, кто первым угадает, выигрывает раунд!
''')