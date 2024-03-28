from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command('help'))
async def get_help(msg: Message):
    await msg.answer("Допомога по навігації в боті")
