from pprint import pprint

from aiogram.filters import CommandStart, Command
from aiogram import Router, F, Bot
from aiogram.types import Message, FSInputFile
from keyboards.kbs import get_donut
from middlewares.album_middlewares import AlbumMiddleware

from aiogram.utils.media_group import MediaGroupBuilder


router = Router()

@router.message(CommandStart())
async def get_start(msg: Message, bot: Bot):
    await msg.answer(f"Вітаю! Напишіть мені повідомлення яке я швидко доставлю адміністрації.", parse_mode="html", reply_markup=get_donut())
