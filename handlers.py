from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup

from datetime import datetime

import bot.calls.call_acc as call_acc
import bot.calls.call_cod as call_cod
import bot.calls.call_com as call_com
import bot.calls.call_cou as call_cou
import bot.calls.call_cov as call_cov
import bot.calls.call_gen as call_gen
import bot.calls.call_mag as call_mag
import bot.calls.call_mar as call_mar
import bot.calls.call_web as call_web

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

import database.cruds.crud_acc as crud_acc

import analytics_main as analytics_main

from functools import partial

# КОНЕЧНЫЙ АВТОМАТ (ИЛИ МАШИНА СОСТОЯНИЙ)
class RegistrationForm(StatesGroup):
    wait_name = State() # Состояние для ожидания имени
    wait_age = State() # Состояние для ожидания возраста
    wait_phone = State() # Состояние для ожидания телефона


##################################################### ОБРАБОТЧИК СООБЩЕНИЙ

async def start_command(message: types.Message):
    text = "Привет! Я - VOTE, твой ассистент в изучении программирования! Давай зарегистрируемся, чтобы начать"
    await message.answer(text)
    await RegistrationForm.wait_name.set() 
    text = 'Введи имя'
    await message.answer(text)

async def handle_age(message, state: FSMContext):
    chat_id = message.chat.id
    name = message.text
    await state.update_data(name=name)
    que_acc.register(chat_id, name)
    await RegistrationForm.next()
    text = 'Введи дату рождения\nПример - 30.08.2001'
    await message.answer(text)
     
async def handle_phone(message, state: FSMContext):
    chat_id = message.chat.id
    age = message.text
    await state.update_data(age=age)
    que_acc.update_age(chat_id, age)
    await RegistrationForm.next()
    text = 'Введи телефон родителя\nПример - +79161576749'
    await message.answer(text)
    
async def handle_course(message, state: FSMContext):
    chat_id = message.chat.id
    phone = message.text
    await state.update_data(phone=phone)
    que_acc.update_phone(chat_id, phone)
    await state.finish()
    text = 'Выбери курс'
    markup = key_cou()
    await message.answer(text, reply_markup=markup)

async def menu_command(message: types.Message):
    chat_id = message.chat.id
    text = "Это главное меню"
    markup = key_gen.key_gen_menu(chat_id)
    print('Команда принята')
    await message.answer(text, reply_markup=markup)

##################################################### ОБРАБОТЧИК ВЫЗОВОВ

async def callback_handler(callback_query: types.CallbackQuery, dp: Dispatcher):
    chat_id = callback_query.message.chat.id
    message = callback_query.message
    await message.delete()
    
    course = que_acc.check_course(chat_id)

    if callback_query.data == 'menu':
        text = "Главное меню"
        markup = key_gen.key_gen_menu(chat_id)
        result = [text, markup]

    elif 'acc_' in callback_query.data:
        result = call_acc.call_account(callback_query)
    elif 'cod_' in callback_query.data:
        result = call_cod.call_codium(callback_query)
    elif 'com_' in callback_query.data:
        result = call_com.call_community(callback_query)
    elif 'cou_' in callback_query.data:
        result = call_cou.call_courses(callback_query)
    elif 'cov_' in callback_query.data:
        result = call_cov.call_covode(callback_query)
    elif 'gen_' in callback_query.data:
        result = call_gen.call_general(callback_query)
    elif 'mag_' in callback_query.data:
        result = call_mag.call_magica(callback_query)
    elif 'mar_' in callback_query.data:
        result = call_mar.call_market(callback_query)
    elif 'web_' in callback_query.data:
        result = call_web.call_webinars(callback_query)

    if result[0] is None: # если текст НЕ задан, а клавиатура есть/нет
        text = 'В разработке'
        await message.answer(text, reply_markup=result[1])
    if result[0] is not None: # если текст задан, а клавиатура есть/нет     
        await message.answer(text = result[0], reply_markup=result[1])
    if result[2] is not None: # если есть картинка
        with open(result[2], 'rb') as photo:
            await dp.bot.send_photo(chat_id=chat_id, photo=photo, caption=result[0], reply_markup=result[1])
    

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(handle_age, state=RegistrationForm.wait_name)
    dp.register_message_handler(handle_phone, state=RegistrationForm.wait_age)
    dp.register_message_handler(handle_course, state=RegistrationForm.wait_phone)
    dp.register_message_handler(menu_command, commands=['menu'])
    partial_callback_handler = partial(callback_handler, dp=dp)
    dp.register_callback_query_handler(partial_callback_handler)