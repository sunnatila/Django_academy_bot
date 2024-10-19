from aiogram import types
from aiogram.filters import CommandStart, Filter, BaseFilter

from data.config import ADMINS
from keyboards.default import admin_menu
from loader import dp

class AdminFilter(BaseFilter):
    async def __call__(self, msg: types.Message,  *args, **kwargs):
        return str(msg.from_user.id) in ADMINS


@dp.message(CommandStart(), AdminFilter())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\n"
                         f"Admin panelga xush kelibsiz.☺️", reply_markup=admin_menu)


@dp.message(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu alaykum xurmatli, {message.from_user.full_name}!\n"
                         f"Django academy botiga xush kelibsiz.☺️\n"
                         f"Botimizdan foydalanish uchun telefon raqamingizni yuboring.")

