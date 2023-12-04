"""КЛАВИАТУРЫ РАЗДЕЛА КОМЬЮННИТИ"""
"""ШИФР РАЗДЕЛА - com"""

from aiogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button

# клавиатура раздела Коммьюнити
def key_com():
    markup = Markup(row_width=1)
    btn_1 = Button('Пати', callback_data='com_party')
    btn_2 = Button('Проекты', callback_data='com_projects')
    btn_3 = Button('Трекинг', callback_data='com_tracking')
    btn_4 = Button('Рейтинг', callback_data='com_rating')
    btn_5 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3, btn_4, btn_5)
    return markup

# клавиатура подраздела Пати раздела Коммьюнити
def key_com_party():
    markup = Markup(row_width=1)
    btn_1 = Button('Мое Пати', callback_data='com_party_me')
    btn_2 = Button('Создать Пати', callback_data='com_party_create')
    btn_3 = Button('Сменить Пати', callback_data='com_party_change')
    btn_4 = Button('Назад', callback_data='com')
    markup.add(btn_1, btn_2, btn_3, btn_4)
    return markup

# клавиатура подраздела Проекты раздела Коммьюнити
def key_com_projects():
    markup = Markup(row_width=1)
    btn_1 = Button('Назад', callback_data='com')
    markup.add(btn_1)
    return markup

# клавиатура подраздела Трекинг раздела Коммьюнити
def key_com_tracking():
    markup = Markup(row_width=1)
    btn_1 = Button('Назад', callback_data='com')
    markup.add(btn_1)
    return markup

# клавиатура подраздела Рейтинг раздела Коммьюнити
def key_com_rating():
    markup = Markup(row_width=1)
    btn_1 = Button('Назад', callback_data='com')
    markup.add(btn_1)
    return markup