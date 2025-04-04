import json
from aiogram.types import Message
from aiogram.filters import Command
from loader import router,cursor,con,admin_id,bot
import random

from aiogram.types import Message
from aiogram.filters import Command
from loader import router, cursor, con, admin_id


@router.message(Command('start_game'))
async def dgfs(message: Message):
    cursor.execute("SELECT * FROM user")
    id_user = message.chat.id
    u=0
    for i in admin_id:
        if i == id_user:
            u=1
    if u==0:
        await message.answer(text='НЕТ ДОСТУПа')
        return
    data = cursor.fetchall()
    random.shuffle(data)
    with open('data/data.json', encoding='utf-8') as file:
        prize= json.loads(file.read())
    text = ('Розыгрыш завершен!\n'
            'Поздравляем победителей с победой:\n'
            )
    for i in range(1):
        text += f'{data[i][1]} - {prize[i]}\n'
    for user in data:
        try:
            await bot.send_message(text=text, chat_id = user[0])
        except:
            pass
    cursor.execute('UPDATE status_reg SET status = (?) WHERE status = (?)', ('False', 'True'))
    con.commit()
    cursor.execute('DELETE FROM user')
    con.commit()