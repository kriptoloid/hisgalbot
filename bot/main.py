import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from config import token
from handlers import c_help, c_start, c_donut, media, answer

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode="MarkdownV2"))
    dp = Dispatcher()
    dp.include_routers(c_help.router, c_donut.router, c_start.router, answer.router, media.user_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=["message", "inline_query", "callback_query"])


if __name__ == "__main__":
    asyncio.run(main())
