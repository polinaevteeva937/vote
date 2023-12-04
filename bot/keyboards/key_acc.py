"""КЛАВИАТУРЫ РАЗДЕЛА АККАУНТ"""
"""ШИФР РАЗДЕЛА - acc"""

from aiogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button

# клавиатура раздела Аккаунт
def key_acc():
    markup = Markup(row_width=1)
    btn_1 = Button('Данные', callback_data='acc_data')
    btn_2 = Button('Портфолио', callback_data='acc_portfolio')
    btn_3 = Button('Прогресс', callback_data='acc_progress')
    btn_4 = Button('Достижения', callback_data='acc_achievements')
    btn_5 = Button('Сертификаты', callback_data='acc_certificates')
    btn_6 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6)
    return markup

# клавиатура подраздела Данные раздела Аккаунт
def key_acc_data():
    markup = Markup(row_width=1)
    btn_1 = Button('Изменить', callback_data='acc_data_change')
    btn_2 = Button('Назад', callback_data='acc_')
    markup.add(btn_1, btn_2)
    return markup

# клавиатура изменения подраздела Данные раздела Аккаунт
def key_acc_data_change():
    markup = Markup(row_width=1)
    btn_1 = Button('Имя', callback_data='acc_data_change_name')
    btn_2 = Button('Дата рождения', callback_data='acc_data_change_age')
    btn_3 = Button('Телефон', callback_data='acc_data_change_phone')
    btn_4 = Button('Курс', callback_data='gen_courses')
    btn_5 = Button('Назад', callback_data='acc_data')
    markup.add(btn_1, btn_2, btn_3, btn_4, btn_5)
    return markup

def key_acc_progress():
    markup = Markup()
    btn_1 = Button('День', callback_data='acc_progress_day')
    btn_2 = Button('Неделя', callback_data='acc_progress_week')
    btn_3 = Button('Месяц', callback_data='acc_progress_month')
    btn_4 = Button('3месяца', callback_data='acc_progress_3month')
    btn_5 = Button('Назад', callback_data='acc_')
    markup.row(btn_1, btn_2)
    markup.row(btn_3, btn_4)
    markup.row(btn_5)
    return markup