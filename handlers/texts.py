from aiogram import Router,F
from aiogram.types import Message,ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from keyboards.inline import dif_choice

user_teams = {}
team_scores = {"ALPHA": 0, "BETA": 0}
router = Router()

@router.message(F.text.in_({'ALPHA','BETA'}))
async def choose_difficulty(message:Message):
    team = message.text
    user_teams[message.from_user.id] = team

    #await message.answer(text=f'Your team is {team}',reply_markup=ReplyKeyboardRemove())

    await message.reply(text='''1.Easy(Легкий)
Words are simple and common (e.g., "apple", "cat", "car")'Слова простые и знакомые (например, «яблоко», «кот», «машина»).'

2.Medium(Средний)
Words are a bit more challenging (e.g., "elephant", "mountain", "guitar")'Слова немного сложнее (например, «слон», «гора», «гитара»).'

3.Hard(Сложный)
Words are more complex and obscure (e.g., "astronaut", "submarine", "philosophy")'Слова более сложные и редкие (например, «астронавт», «подводная лодка», «философия»).'
''',reply_markup=dif_choice())


@router.message(F.text == "END")
async def end_game(message: Message):
    user_id = message.from_user.id
    team = user_teams.get(user_id)

    if team:
        await message.answer(
            f"Game Over! {team} ended the game.\n\n"
            f"🏆 Final Score:\nALPHA: {team_scores['ALPHA']} | BETA: {team_scores['BETA']}"
        )
        team_scores['ALPHA'] = 0
        team_scores['BETA'] = 0

    else:
        await message.answer("You are not in a team!")

    await message.answer("Game has ended. Scores refreshed!\nIf you want start a new game please restart the bot'/start'", reply_markup=ReplyKeyboardRemove())
