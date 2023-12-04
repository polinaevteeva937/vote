import database.cruds.crud_acc as crud_acc
import database.cruds.crud_cod as crud_cod
import database.cruds.crud_com as crud_com
import database.cruds.crud_cou as crud_cou
import database.cruds.crud_cov as crud_cov
import database.cruds.crud_gen as crud_gen
import database.cruds.crud_mag as crud_mag
import database.cruds.crud_mar as crud_mar
import database.cruds.crud_web as crud_web
from datetime import date

# СОЗДАНИЕ ДОМАШКИ
def magica_create(course_id, block_id, order_id, points, answer, condition):
    crud_mag.insert_hometask(course_id, block_id, order_id, points, answer, condition)

# УДАЛЕНИЕ ДОМАШКИ
def magica_delete():
    crud_mag.delete_hometask()

# ПОЛУЧЕНИЕ ДОМАШЕК ИЗ БЛОКА
def get_block(course_id, block_id):
    block_list = crud_mag.select_block(course_id, block_id)
    block_str = ''
    for homework in block_list:
        block_str += f'№ДЗ - {homework[3]} - Баллы - {homework[5]} - Условие - {homework[7]} \n'
    return block_str

def get_hometask(task_id):
    hometask = crud_mag.select_hometask(task_id)
    return hometask