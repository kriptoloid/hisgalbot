from aiogram import types

def give_answer(user_id):
    buttons = [
        [types.InlineKeyboardButton(text="✉️Відповісти", callback_data=f"rm{user_id}")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def get_donut():
    buttons = [
        [types.InlineKeyboardButton(text="🍩Донат", callback_data="donut")],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
