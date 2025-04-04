from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from loader import router


@router.message(Command('cancel'))
async def cacancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Действие отменено')
