import sqlite3

from aiogram import types, Dispatcher
from config import bot
from keyboards.inline_buttons import question_one_keybord
from database.sql_commands import Database


async def start_question(call: types.CallbackQuery):
    print(call)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="are you tired",
        reply_markup=await question_one_keybord()
    )

async def yes_anwser(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="you may go home"
    )
    try:
        Database().sql_insert_user_answer_query(
            telegram_id=call.message.from_user.id,
            username=call.message.from_user.username,
            answer="yes"
        )
    except sqlite3.IntegrityError:
        pass

async def no_anwser(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="you may stay"
    )
    try:
        Database().sql_insert_user_answer_query(
            telegram_id=call.from_user.id,
            username=call.from_user.username,
            answer="no"
        )
    except sqlite3.IntegrityError:
        pass


def register_callback_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_question, lambda call: call.data == "start_question")
    dp.register_callback_query_handler(yes_anwser, lambda call: call.data == "yes_button")
    dp.register_callback_query_handler(no_anwser, lambda call: call.data == "no_button")


