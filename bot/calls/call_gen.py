"""ВЫЗОВЫ ОБЩИЕ"""
"""ШИФР РАЗДЕЛА - gen"""

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


def call_general(callback_query):
    chat_id = callback_query.from_user.id
    
    if callback_query.data == "gen_webinars":
        text = 'Это Вебинары - здесь можно зайти на урок, проверить расписание и баланс'
        markup = key_web.key_web()
        return [text, markup]
    
    elif callback_query.data == "gen_courses":
        text = 'Это Курсы - здесь можно прочитать про курс или сменить его'
        markup = key_cou.key_cou()
        return [text, markup]

    elif callback_query.data == "gen_account":
        text = "Это Аккаунт - здесь можно проверить свои успехи в обучении"
        markup = key_acc.key_acc()
        return [text, markup]

    elif callback_query.data == "gen_covode":
        text = "Это Ководство - здесь можно получию теорию и обновить знания"
        # функция определения курса ученика!
        course = que_acc.check_course(chat_id)
 
        if course == 'frontend':
            markup = key_cov.key_cov_frontend()
        elif course == 'backend':
            markup = key_cov.key_cov_backend()
        elif course == 'analytics':
            markup = key_cov.key_cov_analytics()
        elif course == 'data_science':
            markup = key_cov.key_cov_ds()
        return [text, markup]
        
    elif callback_query.data == "gen_codium":
        tex = "Это Кодиум - здесь можно отработать практические навыки"
        # функция определения курса ученика!
        course = que_acc.check_course(chat_id)

        if course == 'frontend':
            markup = key_cod.key_cod_frontend()
        elif course == 'backend':
            markup = key_cod.key_cod_backend()
        elif course == 'analytics':
            markup = key_cod.key_cod_analytics()
        elif course == 'data_science':
            markup = key_cod.key_cod_ds()
        return [text, markup]

    elif callback_query.data == "gen_community":
        text = "Это Коммьюнити - здесь можно познакомиться с другими студентами"
        markup = key_com.key_com()
        return [text, markup]

    elif callback_query.data == "gen_market":
        text = "Это Маркет - здесь можно исследовать проекты и добавлять свои"
        markup = key_mar.key_mar()
        return [text, markup]