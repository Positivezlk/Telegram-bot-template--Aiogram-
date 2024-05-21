from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router, F
from aiogram import types
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from states import Form
from aiogram.fsm.context import FSMContext

from functions import adding_nums_ask

router = Router()

@router.callback_query(F.data == 'function_1')
async def func_1(callback: types.CallbackQuery, state: FSMContext) -> None:
    await adding_nums_ask(callback.message, state)
