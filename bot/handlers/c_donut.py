from aiogram.filters import Command
from aiogram import Router, F, Bot
from aiogram.types import Message
from keyboards.kbs import get_donut

router = Router()

@router.message(Command('donut'))
async def donut(msg: Message, bot: Bot):
    await msg.answer(f"<b>{msg.from_user.full_name}</b>, будемо дуже вдячні за підтримку проекту", parse_mode="html", reply_markup=get_donut())