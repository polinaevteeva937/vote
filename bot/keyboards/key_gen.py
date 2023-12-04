"""КЛАВИАТУРЫ ОБЩИЕ"""
"""ШИФР РАЗДЕЛА - gen"""

from aiogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button

from bot.queries.que_acc import check_course

# клавиатура для функций в разработке
def key_gen_dev():
    markup = Markup()
    btn_1 = Button('Меню', callback_data='menu')
    markup.add(btn_1)
    return markup

# клавиатура выбора направлений при регистрации
def key_gen_course():
    markup = Markup()
    btn_2 = Button('Frontend', callback_data='gen_choose_frontend')
    btn_3 = Button('Backend', callback_data='gen_choose_backend')   
    btn_4 = Button('Analytics', callback_data='gen_choose_analytics')
    btn_5 = Button('Data Science', callback_data='gen_choose_data_science')
    markup.row(btn_2, btn_3)
    markup.row(btn_4, btn_5)
    return markup

# клавиатура главного меню
def key_gen_menu(chat_id):
    course = check_course(chat_id)

    markup = Markup(row_width=2)
    btn_1 = Button('Уроки', callback_data='gen_webinars')
    btn_2 = Button('Курсы', callback_data='gen_courses')
    markup.add(btn_1, btn_2)

    btn_3 = Button('Волшебка', callback_data='mag_frontend')
    if course == 'backend':
        btn_3 = Button('Волшебка', callback_data='mag_backend')
    elif course == 'analytics':
        btn_3 = Button('Волшебка', callback_data='mag_analytics')
    elif course == 'data_science':
        btn_3 = Button('Волшебка', callback_data='mag_data_science')
    markup.add(btn_3)

    btn_4 = Button('Аккаунт', callback_data='acc_')
    markup.add(btn_4)

    btn_5 = Button('Ководство', callback_data='cov_frontend')
    if course == 'backend':
        btn_5 = Button('Ководство', callback_data='cov_backend')
    elif course == 'analytics':
        btn_5 = Button('Ководство', callback_data='cov_analytics')
    elif course == 'data_science':
        btn_5 = Button('Ководство', callback_data='cov_data_science')
    markup.add(btn_5)

    btn_6 = Button('Кодиум', callback_data='cod_frontend')
    if course == 'backend':
        btn_6 = Button('Кодиум', callback_data='cod_backend')
    elif course == 'analytics':
        btn_6 = Button('Кодиум', callback_data='cod_analytics')
    elif course == 'data_science':
        btn_6 = Button('Кодиум', callback_data='cod_data_science')
    markup.add(btn_6)

    btn_7 = Button('Коммьюнити', callback_data='com_')
    btn_8 = Button('Маркет', callback_data='mar_')
    markup.add(btn_7, btn_8)
    return markup

