from aiogram import types
from aiogram.filters import CommandStart, Command

from apps.models import TgUser
from tlgbot.bot.loader import dp


@dp.message(CommandStart())
async def bot_start(message: types.Message):
    data = {
        'first_name': message.from_user.first_name,
        'username': message.from_user.username,
        'last_name': message.from_user.last_name
    }
    await TgUser.objects.aget_or_create(id=message.from_user.id, **data)
    await message.answer(f"Salom, {message.from_user.full_name}!")


@dp.message(Command(commands=['count']))
async def bot_start(message: types.Message):

    soni = await TgUser.objects.acount()
    await message.answer(f"Jami soni: {soni}!")
