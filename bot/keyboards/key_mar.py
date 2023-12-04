"""КЛАВИАТУРЫ РАЗДЕЛА МАРКЕТ"""
"""ШИФР РАЗДЕЛА - mar"""

from aiogram.types import InlineKeyboardMarkup as Markup, InlineKeyboardButton as Button

# клавиатура раздела Маркет
def key_mar():
    markup = Markup(row_width=1)
    btn_1 = Button('Офферы', callback_data='mar_offers')
    btn_2 = Button('Публикация', callback_data='mar_publish')
    btn_3 = Button('Трансферы', callback_data='mar_transfers')
    btn_4 = Button('Назад', callback_data='menu')
    markup.add(btn_1, btn_2, btn_3, btn_4)
    return markup                 

# клавиатура поздраздела Офферы раздела Маркет
def key_mar_offers():
    markup = Markup()
    btn_1 = Button('Пред. стр', callback_data='mar_offers_prev')
    btn_2 = Button('След. стр', callback_data='mar_offers_next')
    btn_3 = Button('Выбрать', callback_data='mar_offers_pick')
    btn_4 = Button('Назад', callback_data='mar')
    markup.row(btn_1, btn_2)
    markup.row(btn_3)
    markup.row(btn_4)
    return markup

# клавиатура поздраздела Публикация раздела Маркет
def key_mar_publish():
    markup = Markup(row_width=1)
    btn_1 = Button('Опубликовать', callback_data='mar_publish_create')
    btn_2 = Button('Назад', callback_data='mar')
    markup.add(btn_1, btn_2)
    return markup

# клавиатура поздраздела Трансферы раздела Маркет
def key_mar_transfers():
    markup = Markup(row_width=1)
    btn_1 = Button('Перевод студенту', callback_data='mar_transfer_student')
    btn_2 = Button('Перевод Пати', callback_data='mar_transfer_party')
    btn_3 = Button('Запросить у Пати', callback_data='mar_transfer_request')
    btn_4 = Button('Назад', callback_data='mar')
    markup.add(btn_1, btn_2, btn_3, btn_4)
    return markup