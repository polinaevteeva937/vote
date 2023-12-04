"""ОПЕРАЦИИ ДЛЯ ТАБЛИЦ РАЗДЕЛА АККАУНТ"""
"""ШИФР РАЗДЕЛА - acc"""

from sqlalchemy import Table, Column, MetaData, select, insert, update, delete, create_engine, and_
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

from datetime import datetime, timedelta

################### СТУДЕНТЫ ###################
def select_student(chat_id):
    query =  select(mod_acc.students).where(mod_acc.students.c.chat_id == chat_id)
    return complete(query).all()

def select_students():
    query =  select(mod_acc.students)
    return complete(query).all()

def insert_student(chat_id, register_date, name, age, phone, course, points, archived):
    values = {"chat_id": chat_id, "register_date": register_date, 'name': name, 'age': age, 'phone': phone, 'course': course, 'points': points, 'archived': archived}
    query = insert(mod_acc.students).values(values) #prefix_with("OR IGNORE")
    return complete(query)

def update_student(chat_id, name = None, age = None, phone = None, course = None, points = None, archived = None):
    student = select_student(chat_id)
    if name is None:
        name = student[0][3]
    if age is None:
        age = student[0][4]
    if phone is None:
        phone = student[0][5]
    if course is None:
        course = student[0][6]
    if points is None:
        points = student[0][7]
    if archived is None:
        archived = student[0][8]
    
    values = {"chat_id": chat_id, 'name': name, 'age': age, 'phone': phone, 'course': course, 'points': points, 'archived': archived}
    query = update(mod_acc.students).where(mod_acc.students.c.chat_id == chat_id).values(values)
    return complete(query)

def delete_student(chat_id):
    query = delete(mod_acc.students).where(mod_acc.students.c.chat_id == chat_id)
    return complete(query)


################### ПРОГРЕСС ###################
def select_progress(chat_id):
    query =  select(mod_acc.progress).where(mod_acc.progress.c.chat_id == chat_id)
    return complete(query).all()

def select_progress_by_time(chat_id, time_range):
    end_time = datetime.now()

    time_deltas = {
        'day': timedelta(hours=24),
        'week': timedelta(days=7),
        'month': timedelta(weeks=4),
        '3month': timedelta(weeks=12)
    }

    # есть ли такой ключ в словаре
    if time_range in time_deltas:
        # достаем из словаря значение ключа с помощью среза
        delta = time_deltas[time_range]
        # вычисляем начальное время
        start_time = end_time - delta

    query = select(mod_acc.progress).where(
    and_(
        mod_acc.progress.c.chat_id == chat_id,
        mod_acc.progress.c.date >= start_time,
        mod_acc.progress.c.date <= end_time
    )
    )
    return complete(query).all()

def insert_progress(chat_id, link):
    values = {"chat_id": chat_id, "link": link}
    query = insert(mod_acc.progress).values(values)
    return complete(query)

def update_progress(chat_id, link):
    values = {"chat_id": chat_id, "link": link}
    query = update(mod_acc.progress).where(mod_acc.progress.c.chat_id == chat_id).values(values)
    return complete(query)

def delete_progress(chat_id):   
    query = delete(mod_acc.progress).where(mod_acc.progress.c.chat_id == chat_id)
    return complete(query)

################### ПОРТФОЛИО ###################
def select_portfolio(chat_id):
    query =  select(mod_acc.portfolio).where(mod_acc.portfolio.c.chat_id == chat_id)
    return complete(query).all()

def insert_portfolio(chat_id, update_date, route, source_data):
    values = {"chat_id": chat_id, "update_date": update_date, "route": route, "source_data": source_data}
    query = insert(mod_acc.portfolio).values(values)
    return complete(query)

def update_portfolio(chat_id, update_date, route, source_data):
    values = {"chat_id": chat_id, "update_date": update_date, "route": route, "source_data": source_data}
    query = update(mod_acc.portfolio).where(mod_acc.portfolio.c.chat_id == chat_id).values(values)
    return complete(query)

def delete_portfolio(chat_id):
    query = delete(mod_acc.portfolio).where(mod_acc.portfolio.c.chat_id == chat_id)
    return complete(query)


################### ДОСТИЖЕНИЯ ###################
def select_achievement(chat_id, achievement_id):
    query =  select(mod_acc.achievements_bind).where(mod_acc.achievements_bind.c.chat_id == chat_id, mod_acc.achievements_bind.c.achievement_id == achievement_id)
    return complete(query).all()

def select_achievements(chat_id):
    query =  select(mod_acc.achievements_bind).where(mod_acc.achievements_bind.c.chat_id == chat_id)
    return complete(query)

def insert_achievement(level, description, points):
    values = {"level": level, "description": description, "points": points}
    query = insert(mod_acc.achievements).values(values)
    return complete(query)

def assign_achievement(chat_id, achievement_id):
    values = {"chat_id": chat_id, "achievement_id": achievement_id}
    query = insert(mod_acc.achievements_bind).values(values)
    return complete(query)

def update_achievement(achievement_id, level, description, points):
    values = {"level": level, "description": description, "points": points}
    query = insert(mod_acc.achievements).where(mod_acc.achievements.c.achievement_id == achievement_id).values(values)
    return complete(query)

def delete_achievement(achievement_id):
    query = delete(mod_acc.achievements).where(mod_acc.achievements.c.achievement_id == achievement_id)
    return complete(query)


################### СЕРТИФИКАТЫ ###################
def select_certificate(chat_id, certificate_id):
    query =  select(mod_acc.certificates_bind).where(mod_acc.certificates_bind.c.chat_id == chat_id, mod_acc.certificates_bind.c.certificate_id == certificate_id)
    return complete(query).all()

def select_certificates(chat_id):
    query =  select(mod_acc.certificates_bind).where(mod_acc.certificates_bind.c.chat_id == chat_id)
    return complete(query).all()

def insert_certificate(link, description, points):
    values = {"link": link, "description": description, "points": points}
    query = insert(mod_acc.certificates).values(values)
    return complete(query)
    

def assign_certificate(chat_id, certificate_id):
    values = {"chat_id": chat_id, "certificate_id": certificate_id}
    query = insert(mod_acc.certificates_bind).values(values)
    return complete(query)

def update_certificate(certificate_id, link, description, points):
    values = {"link": link, "description": description, "points": points}
    query = insert(mod_acc.certificates).where(mod_acc.certificates.c.certificate_id == certificate_id).values(values)
    return complete(query)

def delete_certificate(certificate_id):
    query = delete(mod_acc.achievements).where(mod_acc.certificates.c.certificate_id == certificate_id)
    return complete(query)