
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router
from aiogram import types
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from states import Form
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(CommandStart())
async def start_bot(message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(text="Функция 1", callback_data='function_1'))
    await message.answer("Привет, это вступительное сообщение.", reply_markup=builder.as_markup())
