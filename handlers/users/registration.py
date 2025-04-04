from aiogram.types import Message
from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from loader import router, cursor, con
from aiogram import F
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_reg

builder = ReplyKeyboardBuilder()

class Form_reg(StatesGroup):
    fio = State()
    numbers = State()
    email = State()
    age = State()
    end = State()


@router.message(F.text == 'Регистрация')
async def start_reg_fun(message: Message, state: FSMContext):
    cursor.execute("SELECT * FROM status_reg")
    if cursor.fetchone()[0] == 'False':
        await message.answer(text='регестрации нет')
        return
    id_user = str(message.chat.id)
    cursor.execute("SELECT * FROM user where id = (?)", [id_user])
    if len(cursor.fetchall()):
        await message.answer(text='вы зарегестрированы')
    await state.update_data(end=False)
    await state.set_state(Form_reg.fio)
    await  message.answer('для начала введите ФИО полностью', reply_markup=types.ReplyKeyboardRemove())


@router.message(Form_reg.fio)
async def get_fio(message: Message, state: FSMContext):
    data = await state.get_data()
    if data['end'] == True:
        await state.update_data(fio=message.text)
        await state.set_state()
        data = await state.get_data()
        fio = data['fio']
        age = data['age']
        numbers = data['numbers']
        email = data['email']
        await state.update_data(end=True)
        for button in kb_reg:
            builder.add(button)
        builder.adjust(1)
        await state.set_state()
        await message.answer('ваши данные:\n' +
                             str(fio) + "\n" +
                             str(numbers) + "\n" +
                             str(email) + "\n" +
                             str(age), reply_markup=builder.as_markup(resize_keyboard=True))
        return
    await state.update_data(fio = message.text)
    await state.set_state(Form_reg.age)
    await message.answer('A теперь введи свой возраст')


@router.message(Form_reg.age)
async def get_fiofafsd(message: Message, state: FSMContext):
    await state.update_data(age = message.text)
    await state.set_state(Form_reg.numbers)
    await message.answer('A теперь введи свой номер')


@router.message(Form_reg.numbers)
async def get_fiofds(message: Message, state: FSMContext):
    await state.update_data(numbers = message.text)
    await state.set_state(Form_reg.email)
    await message.answer('A теперь введи свою почту')


@router.message(Form_reg.email)
async def get_fiofa(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer('uwu')
    data = await state.get_data()
    fio = data['fio']
    age = data['age']
    numbers = data['numbers']
    email = data['email']
    await state.update_data(end=True)
    for button in kb_reg:
        builder.add(button)
    builder.adjust(1)
    await state.set_state()
    await message.answer('ваши данные:\n'+
                         str(fio)+ "\n"+
                         str(numbers)+ "\n"+
                         str(email)+ "\n"+
                         str(age), reply_markup=builder.as_markup(resize_keyboard=True))


@router.message(F.text == 'ФИО')
async def fio_redata(message: Message, state: FSMContext):
    await state.set_state(Form_reg.fio)
    await  message.answer('введите новое ФИО', reply_markup=types.ReplyKeyboardRemove())

@router.message(F.text == 'Все устаивает')
async def fio_final(message: Message, state: FSMContext):
    data = await  state.get_data()
    fio = data['fio']
    age = data['age']
    numbers = data['numbers']
    email = data['email']
    user_id = message.chat.id
    await state.clear()
    cursor.execute('INSERT INTO user (id, FIO, numbers, email, age) VALUES (?,?,?,?,?)',
                   (user_id, fio, numbers, email, age))
    con.commit()
    await  message.answer('все занесененно в таблицу', reply_markup=types.ReplyKeyboardRemove())

@router.message(F.text == 'Номер')
async def fio_redata(message: Message, state: FSMContext):
    await state.set_state(Form_reg.numbers)
    await  message.answer('введите новое Номер', reply_markup=types.ReplyKeyboardRemove())

@router.message(F.text == 'Почта')
async def fio_redata(message: Message, state: FSMContext):
    await state.set_state(Form_reg.email)
    await  message.answer('введите новое Почта', reply_markup=types.ReplyKeyboardRemove())

@router.message(F.text == 'Возраст')
async def fio_redata(message: Message, state: FSMContext):
    await state.set_state(Form_reg.age)
    await  message.answer('введите новое Возраст', reply_markup=types.ReplyKeyboardRemove())
