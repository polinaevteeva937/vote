"""ВЫЗОВЫ РАЗДЕЛА АККАУНТ"""
"""ШИФР РАЗДЕЛА - acc"""

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

import analytics_main

def call_account(callback_query):
    chat_id = callback_query.from_user.id

    if callback_query.data == "acc_":
        text = "Это раздел Аккаунт"
        markup = key_acc.key_acc()
        return [text, markup]

    elif callback_query.data == "acc_data":
        text = "Это Данные аккаунта, здесь можно проверить или изменить их"
        text_2 = que_acc.get_student(chat_id)
        text = f"{text}\n{text_2}"
        markup = key_acc.key_acc_data()
        return [text, markup]
    
    elif callback_query.data == "acc_data_change":
        text = "Выбирите что вы хотите изменить?"
        markup = key_acc.key_acc_data_change()
        return [text, markup]

    elif callback_query.data == "acc_portfolio":
        text = "Это Портфолио аккаунта, здесь видно проекты сделанные самостоятельно или в Пати"
        return [text, None]
    
    elif callback_query.data == "acc_achievements":
        text = "Это Достижения аккаунта, здесь можно полюбоваться на награды"
        return [text, None]

    elif callback_query.data == "acc_certificates":
        text = "Это Сертификаты аккаунта, их можно скачать или загрузить новые"
        return [text, None]
    
    elif callback_query.data == "acc_progress": # обработка нажатия на кнопку Прогресс

        result = handle_progress(callback_query.data, chat_id)
        return result
    
    elif callback_query.data == "acc_progress_day":
        result = handle_progress(callback_query.data, chat_id)
        return result
    
    elif callback_query.data == "acc_progress_week":
        result = handle_progress(callback_query.data, chat_id)
        return result
    
    elif callback_query.data == "acc_progress_month":
        result = handle_progress(callback_query.data, chat_id)
        return result
    
    elif callback_query.data == "acc_progress_3month":
        result = handle_progress(callback_query.data, chat_id)
        return result
    

def handle_progress(callback_data, chat_id):
    # текст для каждой из кнопок
    progress_text = {
        "acc_progress": "Это Прогресс аккаунта, здесь можно просмотреть динамику роста баллов",
        "acc_progress_day": "Это прогресс за текущий день",
        "acc_progress_week": "Это прогресс за текущую неделю",
        "acc_progress_month": "Это прогресс за текущий месяц",
        "acc_progress_3month": "Это прогресс за текущие 3 месяца"
    }

    # Словарь соотносит callback_data с соответствующими параметрами для функции get_progress_by_period
    progress_params = {
        "acc_progress": "day",
        "acc_progress_day": "day",
        "acc_progress_week": "week",
        "acc_progress_month": "month",
        "acc_progress_3month": "3month"
    }

    text = progress_text[callback_data]
    markup = key_acc.key_acc_progress()

    # Вызываем функцию с необходимыми параметрами
    period = progress_params[callback_data]
    progress = que_acc.get_progress_by_period(chat_id, period)
     
    period, points = progress
    photo = analytics_main.get_data(chat_id, period, points)
    return [text, markup, photo]