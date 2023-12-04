"""КЛАВИАТУРЫ РАЗДЕЛА КОВОДСТВО"""
"""ШИФР РАЗДЕЛА - cov"""

from aiogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button

# клавиатура раздела Вебинары
def key_web():
    markup = Markup(row_width=1)
    btn_1 = Button('Войти на урок', callback_data='web_enter')
    btn_2 = Button('Расписание', callback_data='web_schedule')
    btn_3 = Button('Подписка', callback_data='web_subsciption')
    btn_4 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3, btn_4)
    return markup

# клавиатура возврата в Вебинары