"""ВЫЗОВЫ РАЗДЕЛА КОММЬЮНИТИ"""
"""ШИФР РАЗДЕЛА - com"""

import bot.keyboards.key_acc as key_acc
import bot.keyboards.key_cod as key_cod
import bot.keyboards.key_com as key_com
import bot.keyboards.key_cou as key_cou
import bot.keyboards.key_cov as key_cov
import bot.keyboards.key_gen as key_gen
import bot.keyboards.key_mag as key_mag
import bot.keyboards.key_mar as key_mar
import bot.keyboards.key_web as key_web

import bot.queries.que_acc as que_acc
import bot.queries.que_cod as que_cod
import bot.queries.que_com as que_com
import bot.queries.que_cou as que_cou
import bot.queries.que_cov as que_cov
import bot.queries.que_gen as que_gen
import bot.queries.que_mag as que_mag
import bot.queries.que_mar as que_mar
import bot.queries.que_web as que_web

def call_community(callback_query):
    chat_id = callback_query.from_user.id

    if callback_query.data == "com_":
        text = "Это раздел Коммьюнити"
        markup = key_com()
        return [text, markup]

    elif callback_query.data == "com_party":
        text = "Это Пати, здесь можно увидеть свое Пати или выбрать новое"
        markup = key_com.key_com_party()
        return [text, markup]

    elif callback_query.data == "com_projects":
        text = "Это Проекты, здесь отображаются проекты, которые делает Ваша Пати"
        markup = key_com.key_com_projects()
        return [text, markup]

    elif callback_query.data == "com_tracking":
        text = "Это Трекинг, здесь можно посмотреть на вклад участников Пати в проекты"
        markup = key_com.key_com_tracking()
        return [text, markup]

    elif callback_query.data == "com_rating":
        text = "Это Рейтинг, здесь можно увидеть лучшие Пати"
        markup = key_com.key_com_rating()
        return [text, markup]


