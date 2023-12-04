"""ВЫЗОВЫ РАЗДЕЛА КУРСЫ"""
"""ШИФР РАЗДЕЛА - cou"""

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

from bot.queries.que_acc import update_course

def call_courses(callback_query):
    chat_id = callback_query.from_user.id

    if callback_query.data == 'cou_frontend':
        update_course(chat_id, "frontend")
        text = 'Выбери пункт меню'
        markup = key_gen.key_gen_menu(chat_id)
        return [text, markup]

    elif callback_query.data == 'cou_backend':
        update_course(chat_id, "backend")
        text = 'Выбери пункт меню'
        markup = key_gen.key_gen_menu(chat_id)
        return [text, markup]
   
    elif callback_query.data == 'cou_analytics':
        update_course(chat_id, "analytics")
        text = 'Выбери пункт меню'
        markup = key_gen.key_gen_menu(chat_id)
        return [text, markup]
    
    elif callback_query.data == 'cou_data_science':
        update_course(chat_id, "data_science")
        text = 'Выбери пункт меню'
        markup = key_gen.key_gen_menu(chat_id)
        return [text, markup]