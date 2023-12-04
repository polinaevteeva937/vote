"""ВЫЗОВЫ РАЗДЕЛА МАРКЕТ"""
"""ШИФР РАЗДЕЛА - mar"""

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


def call_market(callback_query):
    chat_id = callback_query.from_user.id

    if callback_query.data == "mar_":
        text = "Это раздел Маркет"
        markup = key_mar.key_mar()
        return [text, markup]

    if callback_query.data == "mar_offers":
        text = "Это Офферы, здесь можно вынести проект на голосование (VOTE) в вашей Пати"
        markup = key_mar.key_mar_offers()
        return [text, markup]

    elif callback_query.data == "mar_publish":
        text = "Это Публикация, здесь можно предложить свой Оффер другим Пати"
        markup = key_mar.key_mar_publish()
        return [text, markup]

    elif callback_query.data == "mar_transfers":
        text = "Это Трансферы, здесь можно перевести или запросить баллы другому Пати или студенту"
        markup = key_mar.key_mar_transfers()
        return [text, markup]

    elif callback_query.data == "mar_offers_prev":
        text = "Эта функция в разработке!"
        markup = key_gen.key_gen_dev()
        # функция пролистывания списка офферов на пред.страницу
        return [text, markup]

    elif callback_query.data == "mar_offers_next":
        text = "Эта функция в разработке!"
        markup = key_gen.key_gen_dev()
        # функция пролистывания списка офферов на след.страницу
        return [text, markup]

    elif callback_query.data == "mar_offers_pick":
        text = "Эта функция в разработке!"
        markup = key_gen.key_gen_dev()
        # функция выбора оффера для голосования (vote)
        return [text, markup]

    elif callback_query.data == "mar_publish_create":
        text = "Эта функция в разработке!"
        markup = key_gen.key_gen_dev()
        # функция публикация оффера
        return [text, markup]

    elif callback_query.data == "mar_transfer_student":
        text = "Эта функция в разработке!"
        markup = key_gen.key_gen_dev()
        # функция перевода баллов студенту
        return [text, markup]

    elif callback_query.data == "mar_transfer_party":
        text = "Эта функция в разработке!"
        markup = key_gen.key_gen_dev()
        # функция перевода баллов пати
        return [text, markup]

    elif callback_query.data == "mar_transfer_request":
        text = "Эта функция в разработке!"
        markup = key_gen.key_gen_dev()
        # функция запроса баллов у пати
        return [text, markup]