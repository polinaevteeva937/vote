"""ОПЕРАЦИИ ДЛЯ ТАБЛИЦ РАЗДЕЛА ВОЛШЕБКА"""
"""ШИФР РАЗДЕЛА - mag"""

from sqlalchemy import Table, Column, MetaData, select, insert, update, delete, create_engine
from database_main import complete
import database.models.mod_acc as mod_acc
import database.models.mod_cod as mod_cod
import database.models.mod_com as mod_com
import database.models.mod_cou as mod_cou
import database.models.mod_cov as mod_cov
import database.models.mod_gen as mod_gen
import database.models.mod_mag as mod_mag
import database.models.mod_mar as mod_mar
import database.models.mod_web as mod_web

################### ДОМАШКИ ###################
def select_hometask(task_id):
    query = select(mod_mag.hometasks).where(mod_mag.hometasks.c.task_id == task_id)
    return complete(query).all()

def select_course(course_id):
    query = select(mod_mag.hometasks).where(mod_mag.hometasks.c.course_id == course_id)
    return complete(query).all()

def select_block(course_id, block_id):
    query = select(mod_mag.hometasks).where(mod_mag.hometasks.c.course_id == course_id, mod_mag.hometasks.c.block_id == block_id)
    return complete(query).all()

def select_hometasks(task_id_start, task_id_end):
    query = select(mod_mag.hometasks).where(task_id_start <= mod_mag.hometasks.c.task_id <= task_id_end)
    return complete(query).all()

def insert_hometask(course_id, block_id, order_id, points, answer, condition): #вставка условия
    if len(str(block_id)) != 2:
        block_id = '0' + str(block_id) 
    if len(str(order_id)) != 2:
        order_id = '0' + str(order_id)
    task_id = int(str(course_id) + str(block_id) + str(order_id))
    
    course = ''
    if course_id == 1:
        course = 'frontend'
    elif course_id == 2:
        course = 'backend'
    elif course_id == 3:
        course = 'analytics'
    elif course_id == 4:
        course = 'data_science'
    
   
    values = {'course_id': course_id, 'block_id': block_id, 'order_id': order_id, 'task_id': task_id, 'course': course, 'points': points, 'answer': answer, 'condition': condition}
    query = insert(mod_mag.hometasks).values(values)
    return complete(query)

# дело в том, что при обновлении домашки необязательно я хочу сразу обновлять и points, и answer, и condition
# предположим, что я хочу обновлять только points (кол-во баллов за домашку)
# тогда с frontend'a ключи answer и condition - придут пустые
# но если они придут пустые - то пустые значения могут перезаписать те, что уже есть
# именно поэтому в функции update_hometask я сделаю некоторые параметры - опциональными (необязательными)
# я это делаю благодаря тому, что задаю какие-то значения по умолчанию прям в объявлении
# таким образом при вызове функции update_hometask мне необязательно передавать все параметры

# update_hometask(course_id, block_id, order_id, points)
def update_hometask(course_id, block_id, order_id, points=0, answer="", condition=""): #обновление условия        

    if len(str(block_id)) != 2:
        block_id = '0' + str(block_id) 
    if len(str(order_id)) != 2:
        order_id = '0' + str(order_id)
    task_id = int(str(course_id) + str(block_id) + str(order_id))    

    hometask = select_hometask(task_id)
    if points == 0:
        points = hometask[0][5]
    if answer == '':
        answer = hometask[0][6]
    if condition == '':
        condition = hometask[0][7]

    values = {'points': points, 'answer': answer, 'condition': condition}
    query = update(mod_mag.hometasks).where(mod_mag.hometasks.c.task_id == task_id).values(values)
    return complete(query)

def delete_hometask(task_id): #удаление условия
    query = delete(mod_mag.hometasks).where(mod_mag.hometasks.c.task_id == task_id)
    return complete(query)

def delete_hometasks():
    query = delete(mod_mag.hometasks)
    return complete(query)


################### СТАТУСЫ ###################
def select_status(task_id, student_id): #одиночная выборка статуса
    query =  select(mod_mag.statuses).where(mod_mag.statuses.c.task_id == task_id and mod_mag.statuses.c.student_id == student_id)
    return complete(query).all()

def select_statuses():
    query =  select(mod_mag.statuses)
    return complete(query).all()

def insert_status(course_id, block_id, order_id, student_id, date_from, delivery_status, ready_status): #вставка статуса
    if len(str(block_id)) != 2:
        block_id = '0' + str(block_id)       
    if len(str(order_id)) != 2:
        order_id = '0' + str(order_id)
    task_id = int(str(course_id) + str(block_id) + str(order_id))
    
    values = {'course_id': course_id, 'block_id': block_id, 'order_id': order_id, 'task_id': task_id, 'student_id': student_id, 'date_from': date_from, 'delivery_status': delivery_status, 'ready_status': ready_status}
    query = insert(mod_mag.statuses).values(values)
    return complete(query)

def update_status(task_id, student_id, delivery_status, ready_status, date_from = ''): #обновление статуса
    status = select_status(task_id, student_id)
    if date_from == '':
        date_from = status[0][5]

    values = {'student_id': student_id, 'date_from': date_from, 'delivery_status': delivery_status, 'ready_status': ready_status}
    query = update(mod_mag.statuses).where(mod_mag.statuses.c.task_id == task_id).values(values)
    return complete(query)

def delete_status(task_id, student_id): #удаление статуса
    query = delete(mod_mag.statuses).where(mod_mag.statuses.c.task_id == task_id and mod_mag.reports.c.student_id == student_id)
    return complete(query)


################### РЕПОРТЫ ###################
def select_report(task_id, student_id): #одиночная выборка репорта
    query =  select(mod_mag.reports).where(mod_mag.reports.c.task_id == task_id and mod_mag.reports.c.student_id == student_id)
    return complete(query).all()

def select_reports(task_id_start, task_id_end, student_id_start, student_id_end): #множественная выборка репорта
    query =  select(mod_mag.reports).where(task_id_start < mod_mag.reports.c.task_id < task_id_end and student_id_start < mod_mag.reports.c.student_id < student_id_end)
    return complete(query).all()

def insert_report(course_id, block_id, order_id, student_id, report_data, report_status): #вставка репорта
    if len(str(block_id)) != 2:
        block_id = '0' + str(block_id)       
    if len(str(order_id)) != 2:
        order_id = '0' + str(order_id)    
    task_id = int(str(course_id) + str(block_id) + str(order_id))
    
    values = {'course_id': course_id, 'block_id': block_id, 'order_id': order_id, 'task_id': task_id, 'student_id': student_id, 'report_data': report_data, 'report_status': report_status}
    query = insert(mod_mag.reports).values(values)
    return complete(query)

def update_report(task_id, student_id, report_status, report_data = ''): #обновление репорта
    report = select_report(task_id, student_id)
    if report_data == '':
        report_data = report[0][5]
    
    values = {'student_id': student_id, 'report_data': report_data, 'report_status': report_status}
    query = update(mod_mag.reports).where(mod_mag.reports.c.task_id == task_id).values(values)
    return complete(query)

def delete_report(task_id): #удаление репорта
    query = delete(mod_mag.reports).where(mod_mag.reports.c.task_id == task_id)
    return complete(query)
