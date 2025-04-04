from aiogram import types

kb_start = [
    types.KeyboardButton(text='Регистрация'),
    types.KeyboardButton(text='Информация')
]

kb_game = [
    types.InlineKeyboardButton(text='ставка 10$', callback_data='bet_10'),
    types.InlineKeyboardButton(text='ставка 20$', callback_data='bet_20'),
    types.InlineKeyboardButton(text='ставка 50$', callback_data='bet_50'),
    types.InlineKeyboardButton(text='ставка 100$', callback_data='bet_100')

]

kb_menu =[
    types.InlineKeyboardButton(text='вернуться назад', callback_data='start')
]


kb_reg = [
    types.KeyboardButton(text='ФИО'),
    types.KeyboardButton(text='Возраст'),
    types.KeyboardButton(text='Номер'),
    types.KeyboardButton(text='Почта'),
    types.KeyboardButton(text='Все устраивает')
]