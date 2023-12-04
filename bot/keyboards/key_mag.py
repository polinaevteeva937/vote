"""КЛАВИАТУРЫ РАЗДЕЛА ВОЛШЕБКА"""
"""ШИФР РАЗДЕЛА - mag"""

from aiogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button

# клавиатура раздела Волшебка курса Frontend
def key_mag_frontend():
    markup = Markup(row_width=2)
    btn_1 = Button('Figma', callback_data='mag_figma')
    btn_2 = Button('HTML/CSS', callback_data='mag_html_css')
    btn_3 = Button('Javascript', callback_data='mag_javascript')
    btn_4 = Button('Typescript', callback_data='mag_typescript')
    btn_5 = Button('React', callback_data='mag_react')
    btn_6 = Button('Redux', callback_data='mag_redux')
    btn_7 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7)
    return markup

# клавиатура раздела Волшебка курса Backend
def key_mag_backend():
    markup = Markup(row_width=2)
    btn_1 = Button('Python', callback_data='mag_python')
    btn_2 = Button('Базы данных', callback_data='mag_database')
    btn_3 = Button('API', callback_data='mag_api')
    btn_4 = Button('Деплой', callback_data='mag_deploy')
    btn_5 = Button('Асинхронность', callback_data='mag_async')
    btn_6 = Button('Облако', callback_data='mag_cloud')
    btn_7 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7)
    return markup

# клавиатура раздела Волшебка курса Analytics
def key_mag_analytics():
    markup = Markup(row_width=2)
    btn_1 = Button('Блок 1', callback_data='mag_analytics_1')
    btn_2 = Button('Блок 2', callback_data='mag_analytics_2')
    btn_3 = Button('Блок 3', callback_data='mag_analytics_3')
    btn_4 = Button('Блок 4', callback_data='mag_analytics_4')
    btn_5 = Button('Блок 5', callback_data='mag_analytics_5')
    btn_6 = Button('Блок 6', callback_data='mag_analytics_6')
    btn_7 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7)
    return markup

# клавиатура раздела Волшебка курса Data Science
def key_mag_ds():
    markup = Markup(row_width=2)
    btn_1 = Button('Блок 1', callback_data='mag_ds_1')
    btn_2 = Button('Блок 2', callback_data='mag_ds_2')
    btn_3 = Button('Блок 3', callback_data='mag_ds_3')
    btn_4 = Button('Блок 4', callback_data='mag_ds_4')
    btn_5 = Button('Блок 5', callback_data='mag_ds_5')
    btn_6 = Button('Блок 6', callback_data='mag_ds_6')
    btn_7 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7)
    return markup