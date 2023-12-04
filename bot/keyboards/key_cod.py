"""КЛАВИАТУРЫ РАЗДЕЛА КОДИУМ"""
"""ШИФР РАЗДЕЛА - cod"""

from aiogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button

# клавиатура раздела Кодиум курса Frontend
def key_cod_frontend():
    markup = Markup(row_width=1)
    btn_1 = Button('Типовики', callback_data='cod_typicals_frontend')
    btn_2 = Button('Спидраны', callback_data='cod_speedruns_frontend')
    btn_3 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3)
    return markup

# клавиатура раздела Кодиум курса Backend
def key_cod_backend():
    markup = Markup(row_width=1)
    btn_1 = Button('Типовики', callback_data='cod_typicals_backend')
    btn_2 = Button('Спидраны', callback_data='cod_speedruns_backend')
    btn_3 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3)
    return markup

# клавиатура раздела Кодиум курса Analytics
def key_cod_analytics():
    markup = Markup(row_width=1)
    btn_1 = Button('Типовики', callback_data='cod_typicals_analytics')
    btn_2 = Button('Спидраны', callback_data='cod_speedruns_analytics')
    btn_3 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3)
    return markup            

# клавиатура раздела Кодиум курса Data Science
def key_cod_ds():
    markup = Markup(row_width=1)
    btn_1 = Button('Типовики', callback_data='cod_typicals_ds')
    btn_2 = Button('Спидраны', callback_data='cod_speedruns_ds')
    btn_3 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3)
    return markup     