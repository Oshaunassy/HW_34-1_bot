from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def start_keyboard():
    markup = InlineKeyboardMarkup()
    question_button = InlineKeyboardButton(
        "Start Questoin",
        callback_data="start_question"
    )

    markup.add(question_button)
    return markup

async def question_one_keybord():
    markup = InlineKeyboardMarkup()
    yes_button = InlineKeyboardButton("Yes", callback_data="yes_button")
    no_button = InlineKeyboardButton("No", callback_data="no_button")
    markup.add(yes_button, no_button)
    return markup





