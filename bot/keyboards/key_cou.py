"""КЛАВИАТУРЫ РАЗДЕЛА КУРСЫ"""
"""ШИФР РАЗДЕЛА - cou"""

from aiogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button

# клавиатура раздела Курсы
def key_cou():
    markup = Markup()
    btn_2 = Button('Frontend', callback_data='cou_frontend')
    btn_3 = Button('Backend', callback_data='cou_backend')
    btn_4 = Button('Analytics', callback_data='cou_analytics')
    btn_5 = Button('Data Science', callback_data='cou_ds')
    btn_6 = Button('Меню', callback_data='menu')
    markup.row(btn_2, btn_3)
    markup.row(btn_4, btn_5)
    markup.row(btn_6)
    return markup

# клавиатура курса Frontend
def key_cou_frontend():
    markup = Markup(row_width=1)
    btn_1 = Button('Сменить курс', callback_data='cou_choose_frontend')
    btn_2 = Button('Назад', callback_data='courses')
    markup.add(btn_1, btn_2)
    return markup

# клавиатура курса Backend
def key_cou_backend():
    markup = Markup(row_width=1)
    btn_1 = Button('Сменить курс', callback_data='cou_choose_backend')
    btn_2 = Button('Назад', callback_data='courses')
    markup.add(btn_1, btn_2)
    return markup

# клавиатура курса Analytics
def key_cou_analytics():
    markup = Markup(row_width=1)
    btn_1 = Button('Сменить курс', callback_data='cou_choose_analytics')
    btn_2 = Button('Назад', callback_data='courses')
    markup.add(btn_1, btn_2)
    return markup

# клавиатура курса Data Science
def key_cou_ds():
    markup = Markup(row_width=1)
    btn_1 = Button('Сменить курс', callback_data='cou_choose_ds')
    btn_2 = Button('Назад', callback_data='courses')
    markup.add(btn_1, btn_2)
    return markup