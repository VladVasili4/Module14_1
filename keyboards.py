from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



in_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Для начинающих',callback_data='small')],
    [InlineKeyboardButton(text='Для опытных',callback_data='medium')],
    [InlineKeyboardButton(text='Для профи',callback_data='big')],
    [InlineKeyboardButton(text='Другие предложения',callback_data='other')]])


start_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='О нас')],
    [KeyboardButton(text='Стоимость')]],
                           resize_keyboard=True)


buy_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Купить', url='https://ya.ru/')],
                                               [InlineKeyboardButton(text='Назад', callback_data='back_to_catalog')]])


admin_panel = InlineKeyboardButton(inline_keyboard=[
    [InlineKeyboardButton(text='Пользователи', callback_data='users')]
    [InlineKeyboardButton(text='Статистика', callback_data='stat')]
    [InlineKeyboardButton(text='Блокировка', callback_data='block'),
    InlineKeyboardButton(text='Разблокировка', callback_data='unblock')]] )

