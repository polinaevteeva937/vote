import database.cruds.crud_acc as crud_acc
import database.cruds.crud_cod as crud_cod
import database.cruds.crud_com as crud_com
import database.cruds.crud_cou as crud_cou
import database.cruds.crud_cov as crud_cov
import database.cruds.crud_gen as crud_gen
import database.cruds.crud_mag as crud_mag
import database.cruds.crud_mar as crud_mar
import database.cruds.crud_web as crud_web
from datetime import date, datetime

# new_handlers -> account_queries

# ЗАПИСЫВАЕТ В ТАБЛИЦУ СО СТУДЕНТАМИ НОВОГО СТУДЕНТА
def register(chat_id, name):
    register_date = date.today()
    points = 10
    archived = False
    crud_acc.insert_student(chat_id, register_date=register_date, name=name, points=points, archived=archived)

# ОБНОВЛЕНИЕ ИМЕНИ
def update_name(chat_id, name):
    crud_acc.update_student(chat_id, name=name)

# ОБНОВЛЕНИЕ ДАТЫ РОЖДЕНИЯ
def update_age(chat_id, age):
    crud_acc.update_student(chat_id, age=age)

# ОБНОВЛЕНИЕ ТЕЛЕФОНА
def update_phone(chat_id, phone):
    crud_acc.update_student(chat_id, phone=phone)

# ОБНОВЛЕНИЕ КУРСА
def update_course(chat_id, course):
    crud_acc.update_student(chat_id, course=course)

# ПРОВЕРКА КУРСА
def check_course(chat_id):
    student = crud_acc.select_student(chat_id)
    course = student[0][6]
    return course

# ПОЛУЧЕНИЕ ПРОГРЕССА
def get_progress(chat_id):
    progress = crud_acc.select_progress(chat_id)
    return progress

# ПОЛУЧЕНИЕ ПРОГРЕССА ПО ВРЕМЕНИ
def get_progress_by_period(chat_id, period_type):
    progress = crud_acc.select_progress_by_time(chat_id, period_type)
    
    # progress = [(), ()]
    period = []
    points = []
    
    for record in progress:
        # Преобразуем запись времени в формат "17:00" и добавляем в список period
        formatted_time = datetime.strptime(str(record[2]), "%Y-%m-%d %H:%M:%S").strftime("%m-%d %H:%M")
        period.append(formatted_time)

        # Добавляем соответствующее количество очков в список points
        points.append(record[3])
    
    return [period, points]


# ПОЛУЧЕНИЕ СТУДЕНТА
def get_student(chat_id):
    student = crud_acc.select_student(chat_id)

    # student = [(student_id, chat_id, register_date, name, age, phone, course, points, archived)]
    student_id = str(student[0][0])
    register_date = str(student[0][2])
    name = str(student[0][3])
    age = str(student[0][4])
    phone = str(student[0][5])   
    course = str(student[0][6])
    points = str(student[0][7])
    archived = str(student[0][8])
    result = f'№ студента - {student_id} \n' + \
            f'Дата регистрации - {register_date} \n' + \
            f'Имя - {name} \n' + \
            f'Дата рождения - {age} \n' + \
            f'Телефон - {phone} \n' + \
            f'Курс - {course} \n' + \
            f'Баллы - {points} \n' + \
            f'Архивирован - {archived} '
    return result