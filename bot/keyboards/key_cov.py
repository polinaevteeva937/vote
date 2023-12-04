"""КЛАВИАТУРЫ РАЗДЕЛА КОВОДСТВО"""
"""ШИФР РАЗДЕЛА - cov"""

from aiogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button

# клавиатура раздела Ководство курса Frontend
def key_cov_frontend():
    markup = Markup(row_width=1)
    btn_1 = Button('Компендиум', callback_data='cov_compendium_frontend')
    btn_2 = Button('Записи', callback_data='cov_records_frontend')
    btn_3 = Button('Тесты', callback_data='cov_tests_frontend')
    btn_4 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3, btn_4)
    return markup

# клавиатура раздела Ководство курса Backend
def key_cov_backend():
    markup = Markup(row_width=1)
    btn_1 = Button('Компендиум', callback_data='cov_compendium_backend')
    btn_2 = Button('Записи', callback_data='cov_records_backend')
    btn_3 = Button('Тесты', callback_data='cov_tests_backend')
    btn_4 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3, btn_4)
    return markup 

# клавиатура раздела Ководство курса Analytics
def key_cov_analytics():
    markup = Markup(row_width=1)
    btn_1 = Button('Компендиум', callback_data='cov_compendium_analytics')
    btn_2 = Button('Записи', callback_data='cov_records_analytics')
    btn_3 = Button('Тесты', callback_data='cov_tests_analytics')
    btn_4 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3, btn_4)
    return markup

# клавиатура раздела Ководство курса Data Science
def key_cov_ds():
    markup = Markup(row_width=1)
    btn_1 = Button('Компендиум', callback_data='cov_compendium_ds')
    btn_2 = Button('Записи', callback_data='cov_records_ds')
    btn_3 = Button('Тесты', callback_data='cov_tests_ds')
    btn_4 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3, btn_4)
    return markup       