
from aiogram import types
from aiogram.filters import CommandStart,  StateFilter
from aiogram.fsm.context import FSMContext

from data.config import ADMINS

from loader import dp, db


@dp.message(lambda msg: msg.text == '👥 Guruh yaratish')
async def add_group(msg: types.Message, state: FSMContext):
    await msg.answer("Guruh raqamini kiriting")
    await state.set_state("add_group")


@dp.message(StateFilter("add_group"))
async def add_group_number(msg: types.Message, state: FSMContext):
    group_number = msg.text
    if group_number.isdigit():
        db.add_group(group_number)
        await msg.answer("Guruh muvaffaqiyatli tarzda yaratildi.☺️")
        await state.clear()
    else:
        await msg.answer("Iltimos raqam kiriting!!")
        await state.set_state("add_group")
