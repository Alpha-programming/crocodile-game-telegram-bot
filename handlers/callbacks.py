from aiogram.types import CallbackQuery,Message
from aiogram import Router,F
from deep_translator import  GoogleTranslator
from pathlib import Path
import random
from keyboards.inline import found_kb
from handlers.texts import user_teams,team_scores

BASE_DIR = Path(__name__).resolve().parent
alpha_score = 0
beta_Score = 0

router = Router()
translator = GoogleTranslator()

with open(f'{BASE_DIR}/easy_words_1M.txt', 'r', encoding='utf-8') as easy_file:
    easy_words = easy_file.read().splitlines()

with open(f'{BASE_DIR}/medium_words_1M.txt', 'r', encoding='utf-8') as medium_file:
    medium_words = medium_file.read().splitlines()

with open(f'{BASE_DIR}/hard_words_1M.txt', 'r', encoding='utf-8') as hard_file:
    hard_words = hard_file.read().splitlines()

def translated_word(word):
    return GoogleTranslator(source='en', target='ru').translate(word)

@router.callback_query(F.data.startswith('easy'))
async def easy_level(call: CallbackQuery):
    easy_word = random.choice(easy_words)
    await call.message.edit_text(text=f'{easy_word}-{translated_word(easy_word)}',reply_markup=found_kb())

@router.callback_query(F.data.startswith('medium'))
async def medium_level(call: CallbackQuery):
    medium_word = random.choice(medium_words)
    await call.message.edit_text(text=f'{medium_word}-{translated_word(medium_word)}',reply_markup=found_kb())

@router.callback_query(F.data.startswith('hard'))
async def hard_level(call:CallbackQuery):
    hard_word = random.choice(hard_words)
    await call.message.edit_text(text=f'{hard_word}-{translated_word(hard_word)}',reply_markup=found_kb())

@router.callback_query(F.data.startswith('yes'))
async def found(call: CallbackQuery):
    user_id = call.from_user.id
    team = user_teams.get(user_id)

    if team:
        team_scores[team] += 1
        await call.message.edit_text(
            f"✅ Word Found! {team} gets +1 point! 🎉\n\n"
            f"Current Score:\nALPHA: {team_scores['ALPHA']} | BETA: {team_scores['BETA']}"
        )
    else:
        await call.answer("❌ You are not in a team!", show_alert=True)

@router.callback_query(F.data.startswith('no'))
async def not_found(call: CallbackQuery):
    await call.message.edit_text("❌ Word not found! No points awarded. Try again next time! 🔄")
