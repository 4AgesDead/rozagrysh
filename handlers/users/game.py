from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from loader import router, cursor, Bot, con
from aiogram import F, types
from keys.key import kb_game, kb_menu, kb_start


@router.message(F.text == 'Играем!')
async def game(message: Message):
    await message.answer('Добро пожаловать к нам!', reply_markup=types.ReplyKeyboardRemove())
    id_user = message.chat.id
    cursor.execute("SELECT * FROM kazik where id = (?)", [id_user])
    money = cursor.fetchall()[0][1]
    builder = InlineKeyboardBuilder()
    for button in kb_game:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text=f'Ваш баланс: {money}\nДелаем ставку?',
                         reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(F.data.startswith('bet'))
async def dfgd(callback: types.CallbackQuery, bot: Bot):
    print(423423)
    bet = int(callback.data.split('_')[1])
    id_user = callback.message.chat.id
    cursor.execute("SELECT * FROM kazik where id = (?)", [id_user])
    money_user = cursor.fetchall()[0][1]
    if bet > money_user:
        await  callback.answer(text='Недостаточно средств на счету!')
    else:
        dice_mess = await callback.message.answer_dice(emoji='🎰')
        value_dice = dice_mess.dice.value
        if value_dice < 32:
            cursor.execute("UPDATE kazik set money = (?) where id = (?)", (money_user - bet, id_user))
            con.commit()
            await callback.answer(text='лох твоя карта теперь моя!')
        else:
            cursor.execute("UPDATE kazik set money = (?) where id = (?)", (money_user + bet * 2, id_user))
            con.commit()
            await callback.answer(text='повезло!')
        builder = InlineKeyboardBuilder()
        print()
        for button in kb_game:
            builder.add(button)
        builder.adjust(1)
        await callback.message.answer(text=f'Ваш баланс: {money_user}\nДелаем ставку?',
                             reply_markup=builder.as_markup(resize_keyboard=True))

@router.message(F.text == 'Меню')
async def game(message: Message):
    await message.answer('Добро пожаловать к нам!', reply_markup=types.ReplyKeyboardRemove())
    id_user = message.chat.id
    cursor.execute("SELECT * FROM kazik where id = (?)", [id_user])
    money = cursor.fetchall()[0][1]
    builder = InlineKeyboardBuilder()
    for button in kb_menu:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text=f'Ваш баланс: {money}',
                         reply_markup=builder.as_markup(resize_keyboard=True))

@router.message(F.data.startswith('start'))
async def fun_start(message: Message):
    cursor.execute("SELECT * FROM kazik")
    builder = ReplyKeyboardBuilder()
    id_user = message.chat.id
    tablica = cursor.fetchall()
    print(1)
    if not tablica:
        cursor.execute('INSERT INTO kazik (id) VALUES (?)', [id_user])
        con.commit()
    for button in kb_start:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text='Поиграем?!',
                         reply_markup=builder.as_markup(resize_keyboard=True))