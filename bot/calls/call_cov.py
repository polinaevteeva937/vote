"""ВЫЗОВЫ РАЗДЕЛА КОВОДСТВО"""
"""ШИФР РАЗДЕЛА - cov"""

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


def call_covode(callback_query):
    chat_id = callback_query.from_user.id

    if callback_query.data == "cov_compendium_frontend":
        text = "Это Компендиум курса Frontend"  
        return [text, None]

    elif callback_query.data == "cov_records_frontend":
        text = "Это Вебинары курса Frontend"
        return [text, None]

    elif callback_query.data == "cov_tests_frontend":
        text = "Это Тесты курса Frontend"
        return [text, None]

    elif callback_query.data == "cov_compendium_backend":
        text = "Это Компендиум курса Backend"
        return [text, None]

    elif callback_query.data == "cov_records_backend":
        text = "Это Вебинары курса Backend"
        return [text, None]

    elif callback_query.data == "cov_tests_backend":
        text = "Это Тесты курса Backend"      
        return [text, None]

    elif callback_query.data == "cov_compendium_analytics":
        text = "Это Компендиум курса Analytics"       
        return [text, None]

    elif callback_query.data == "cov_records_analytics":
        text = "Это Вебинары курса Anaytics"
        return [text, None]

    elif callback_query.data == "cov_tests_analytics":
        text = "Это Тесты курса Analytics"
        return [text, None]

    elif callback_query.data == "cov_compendium_ds":
        text = "Это Компендиум курса Data Science"
        return [text, None]

    elif callback_query.data == "cov_records_ds":
        text = "Это Вебинары курса Data Science"
        return [text, None]

    elif callback_query.data == "cov_tests_ds":
        text = "Это Тесты курса Data Science"
        return [text, None]