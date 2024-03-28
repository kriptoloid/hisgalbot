from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery

from middlewares.album_middlewares import AlbumMiddleware
from aiogram.utils.media_group import MediaGroupBuilder

from keyboards.kbs import give_answer
from config import admId

user_router = Router()
user_router.message.middleware(AlbumMiddleware())

@user_router.message(F)
async def get_album(msg: Message, bot: Bot, album: list = None):
    forward = f'Переслане повідомлення <a href=\"tg://user?id={msg.forward_from.id}\">: {msg.forward_from.full_name}</a>' if msg.forward_from != None else ''
    forward_chat = f'Переслане повідомлення з: {msg.forward_from_chat.title}\n@{msg.forward_from_chat.username}' if msg.forward_from_chat != None else ''
    if msg.from_user.id != admId:
        if album:
            album_builder = MediaGroupBuilder()
            for i in album:
                if i.photo:
                    album_builder.add_photo(
                        caption=i.caption if i.caption != None else None,
                        media=i.photo[-1].file_id,
                        parse_mode="html"
                    )
                elif i.video:
                    album_builder.add_video(
                        caption=i.caption if i.caption != None else None,
                        media=i.video.file_id,
                        parse_mode="html"
                    )
            await bot.send_media_group(chat_id=admId, media=album_builder.build())

        else:
            if msg:
                await bot.forward_message(chat_id=admId, message_id=msg.message_id, from_chat_id=msg.from_user.id)
        
        
        await bot.send_message(
            chat_id=admId, 
            text=f"{forward}{forward_chat}\nПовідомлення від <a href='tg://user?id={msg.from_user.id}'>: {msg.from_user.full_name}</a>",
            parse_mode="html", 
            reply_markup=give_answer(msg.from_user.id)
        )
    
    else:
        await msg.answer('Потрібно натиснути кнопку відповіді')
    