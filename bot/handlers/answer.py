from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from utils.state import Form
from keyboards.kbs import give_answer
from aiogram.filters import Command

router = Router()

@router.message(Command("cancel"))
async def cancel_answer(msg: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Відповідь скасована"
    )

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

@router.message(Command("cancel"))
async def cancel_answer(msg: Message, state: FSMContext):
    print("ok")
    await state.clear()
