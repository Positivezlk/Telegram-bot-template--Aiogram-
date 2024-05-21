from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router
from aiogram import types
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from states import Form
from aiogram.fsm.context import FSMContext

from buttons import button_func_1

router = Router()


@router.message(CommandStart())
async def start_bot(message):
    await message.answer("Привет, это вступительное сообщение.", reply_markup=button_func_1.as_markup())
