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

def course_get(course_id):
    hometasks = crud_mag.select_course(course_id)
    return hometasks

def block_get(course_id, block_id):
    if len(str(block_id)) != 2:
        block_id = int("0" + str(block_id))

    hometasks = crud_mag.select_block(course_id, block_id) # hometasks = [('', '', '', 0, 0, 0), ('', '', '', 0, 0, 0)]
    # hometasks - список из словарей
    
    return hometasks

def hometask_get(task_id):
    hometask = crud_mag.select_hometask(task_id) 
    return hometask

def catalog_put(homework):
    
    course_id = homework.course_id
    block_id = homework.block_id
    order_id = homework.order_id
    points = homework.points
    answer = homework.answer
    condition = homework.condition

    crud_mag.insert_hometask(course_id, block_id, order_id, points, answer, condition)

def catalog_patch(homework):
    
    course_id = homework.course_id
    block_id = homework.block_id
    order_id = homework.order_id
    points = homework.points
    answer = homework.answer
    condition = homework.condition

    crud_mag.update_hometask(course_id, block_id, order_id, points, answer, condition)

def catalog_post(data):
    hw_id = data['id_hometask']
    student_id = data['id_student']
    deadline = data['deadline']
    message_for_front = f'deadline: {deadline}, student_id: {student_id}, hw_id: {hw_id}'

    return message_for_front

def status_get():
    statuses = crud_mag.select_statuses()
    

    
def report_get():
    reports = crud_mag.select_reports()
    big_reports = []
    for report in reports: # big_hometasks = [{cou: 1, blo: 1, ord: 1, tas: 10101, cou: 'web'}, {cou: 1, blo: 1, ord: 1, tas: 10101, cou: 'web'}]
        data = {
            "report_id": reports[0],
            "task_id": reports[1],
            "student_id": reports[2],
            "when": reports[3],
            "status": reports[4],
            "cause": reports[5],
        }
        big_reports.append(data)
        return big_reports