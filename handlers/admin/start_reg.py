from aiogram.types import Message
from aiogram.filters import Command
from loader import router, cursor, con, admin_id


@router.message(Command('start_reg'))
async def fun_start(message: Message):
    cursor.execute("SELECT * FROM user")
    id_user = message.chat.id
    u=0
    for i in admin_id:
        if i == id_user:
            u=1
    if u==0:
        await message.answer(text='НЕТ ДОСТУПа')
        return
    cursor.execute('UPDATE status_reg SET status = (?) WHERE status = (?)', ('True','False'))
    con.commit()
    await message.answer(text='команда выполнена')
