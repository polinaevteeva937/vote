"""ВЫЗОВЫ РАЗДЕЛА ВОЛШЕБКА"""
"""ШИФР РАЗДЕЛА - mag"""

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


def get_magica_block(course, block_number):
    course_name = {
        # будет 24 строки (4 курса по 6 блоков)
        "figma": "Figma курса Frontend",
        "html_css": "HTML/CSS курса Frontend",
        "javascript": "Javascript курса Frontend",
        "typescript": "Typescript курса Frontend",
        "react": "React курса Frontend",
        "redux": "Redux курса Frontend",
        "python": "Python курса Backend",
        "database": "Базы данных курса Backend",
        "api": "API курса Backend",
        "deploy": "Деплой курса Backend",
        "async":"Асинхронность курса Backend",
        "cloud": "Облако курса Backend",
        "analytics_1": "1 курса Аналитики",
        "analytics_2": "2 курса Аналитики",
        "analytics_3": "3 курса Аналитики",
        "analytics_4": "4 курса Аналитики",
        "analytics_5": "5 курса Аналитики",
        "analytics_6": "6 курса Аналитики",
        "ds_1": "1 курса Data Science",
        "ds_2": "2 курса Data Science",
        "ds_3": "3 курса Data Science",
        "ds_4": "4 курса Data Science",
        "ds_5": "5 курса Data Science",
        "ds_6": "6 курса Data Science"
    }

    block_name = que_mag.get_block(course, block_number)
    return f"Это Волшебка блока {course_name[course]} \n + block_name"
           


def call_magica(callback_query):
    chat_id = callback_query.from_user.id

    if callback_query.data == "mag_frontend":
        text = "Это Волшебка курса Frontend - здесь можно найти домашнее задание и решить его"
        markup = key_mag.key_mag_frontend()
        return [text, markup]

    elif callback_query.data == "mag_backend":
        text = "Это Волшебка курса Backend - здесь можно найти домашнее задание и решить его"
        markup = key_mag.key_mag_backend()
        return [text, markup]

    elif callback_query.data == "mag_analytics":
        text = "Это Волшебка курса Analytics - здесь можно найти домашнее задание и решить его"
        markup = key_mag.key_mag_analytics()
        return [text, markup]

    elif callback_query.data == "mag_data_science":
        text = "Это Волшебка курса Data Science - здесь можно найти домашнее задание и решить его"
        markup = key_mag.key_mag_ds()
        return [text, markup]

    
    elif callback_query.data == "mag_figma":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_html_css":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_javascript":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_typescript":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_react":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_redux":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]
        
    elif callback_query.data == "mag_python":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_database":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_api":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_deploy":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_async":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_cloud":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_analytics_1":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]
    
    elif callback_query.data == "mag_analytics_2":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_analytics_3":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_analytics_4":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_analytics_5":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_analytics_6":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_ds_1":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_ds_2":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_ds_3":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_ds_4":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_ds_5":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]

    elif callback_query.data == "mag_ds_6":
        course, block_number = callback_query.data.split("_")[-2:]
        text = get_magica_block(course, block_number)
        return [text, None]