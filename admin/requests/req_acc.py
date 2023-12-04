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

def students_get():
    x = crud_acc.select_students()
    students_dicts = list(map(lambda x: dict(student_id = x[0], \
                                             chat_id = x[1],
                                             register_date = x[2], \
                                             name = x[3] , \
                                             age = x[4] , \
                                             phone = x[5] , \
                                             course = x[6] , \
                                             points = x[7] , \
                                             archived = x[8]                                             
                                             ), x))
    return students_dicts

def student_get(chat_id):
    x = crud_acc.select_student(chat_id)
    student_dict = list(map(lambda x: dict(student_id = x[0], \
                                             chat_id = x[1],
                                             register_date = x[2], \
                                             name = x[3] , \
                                             age = x[4] , \
                                             phone = x[5] , \
                                             course = x[6] , \
                                             points = x[7] , \
                                             archived = x[8]                                             
                                             ), x))
    return student_dict

def students_put(chat_id, register_date, name, age, phone, course, points, archived):
    crud_acc.insert_student(chat_id, register_date, name, age, phone, course, points, archived)

def students_patch(chat_id, name, age, phone, course, points, archived):
    crud_acc.update_student(chat_id, name, age, phone, course, points, archived)

def students_post():
    pass

def students_filter():
    pass

def students_delete(chat_id):
    crud_acc.delete_student(chat_id)

def portfolio_get():
    pass 

def portfolio_put(): 
    pass

def portfolio_patch():
    pass

def portfolio_delete():
    pass

def progress_get():
    pass

def achievements_put():
    pass


def achievements_get():
    pass


def achievements_patch():
    pass


def achievements_delete():
    pass


def certificates_get():
    pass


def certificates_put():
    pass


def certificates_patch():
    pass

def certificates_delete():
    pass