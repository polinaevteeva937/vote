"""ВЫЗОВЫ РАЗДЕЛА ВЕБИНАРЫ"""
"""ШИФР РАЗДЕЛА - web"""

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


def call_webinars(callback_query):
    chat_id = callback_query.from_user.id

    if callback_query.data == "web_enter":
        text = "Это Вход на урок - а точнее на сервер Discord - https://discord.gg/4sdWQjjEd9 "
        # здесь функция, которая делает запрос Дискорд боту
        return [text, None]

    elif callback_query.data == "web_schedule":
        text = "Это Расписание преподавателя "
        # здесь функция, которая делает запрос к Google API
        return [text, None]

    elif callback_query.data == "web_subscription":
        text = "Это Подписка на вебинары и платный контент"
        # здесь функция проверки подписки и интеграция с UMoney
        return [text, None]