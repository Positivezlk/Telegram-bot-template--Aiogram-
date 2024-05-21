from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from states import Form

router = Router()


@router.message(Form.function1)
async def adding_nums_ask(message: Message, state: FSMContext):
    await state.set_state(Form.function1_2)
    await message.answer('Напиши 2 числа через пробел')



@router.message(Form.function1_2)
async def adding(message: Message, state: FSMContext):
    await state.update_data(function1_2=message.text)
    data = await state.get_data()
    a, b = data['function1_2'].split(' ')
    if a.isdigit() and b.isdigit():  
        await message.answer(f'{a} + {b} = {int(a) + int(b)}')
    else:
        await message.answer('Неправильный ввод! Можно вводить только числа, и только через пробел.')
        await state.set_state(Form.function1)
        await adding_nums_ask(message, state)
        