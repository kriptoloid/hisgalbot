from pprint import pprint

from aiogram.filters import CommandStart, Command
from aiogram import Router, F, Bot
from aiogram.types import Message
from keyboards.kbs import get_donut

router = Router()

@router.message(CommandStart())
async def get_start(msg: Message, bot: Bot):
    print(msg.from_user.id)
    await msg.answer(f"👋Вітаю! Напишіть мені повідомлення яке я швидко доставлю адміністрації.", parse_mode="html", reply_markup=get_donut())
