from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_start
from loader import router, con, cursor
import sqlite3


@router.message(Command('start'))
async def fun_start(message: Message):
    cursor.execute("SELECT * FROM user")
    builder = ReplyKeyboardBuilder()
    id_user = message.chat.id
    for button in kb_start:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text='Добро пожаловать!',
                         reply_markup=builder.as_markup(resize_keyboard=True))
