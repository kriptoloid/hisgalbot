from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from utils.state import Form
from keyboards.kbs import give_answer
from aiogram.filters import Command

router = Router()


@router.callback_query(F.data.startswith("rm"))
async def send_random_value(callback: CallbackQuery, state: FSMContext,):
    await state.update_data(user_id=callback.data[2:])
    await callback.answer("Окей, напиши відповідь")
    await state.set_state(Form.answer)

@router.message(Form.answer)
async def answer(msg: Message, state: FSMContext, bot: Bot):
    user_data = await state.get_data()
    await msg.send_copy(user_data['user_id'])
    await state.clear()
