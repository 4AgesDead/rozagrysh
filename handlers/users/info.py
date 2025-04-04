from aiogram.types import Message
from loader import router
from aiogram import F, types


@router.message(F.text == 'Информация')
async def game(message: Message):
    file = open('data/info.txt', encoding= 'utf-8')
    info = file.read()
    await message.answer(text=info, reply_markup=types.ReplyKeyboardRemove())