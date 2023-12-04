"""МОДЕЛИ ТАБЛИЦ РАЗДЕЛА ВОЛШЕБКА"""
"""ШИФР РАЗДЕЛА - mag"""

from sqlalchemy import Table, Column, MetaData, select, insert, update, delete, create_engine
from sqlalchemy.types import Integer, Float, Text, Date, DateTime, Boolean
from database_main import engine
metadata = MetaData()

# ТАБЛИЦА ДЗ
hometasks = Table("hometasks", metadata, \
            Column("course_id", Integer), #номер курса !6 курсов
            Column("block_id", Integer), #номер блока 
            Column("order_id", Integer), #номер порядка 
            Column("task_id", Integer, primary_key=True, unique=True), #номер задания !пятизначное число 10203 (1 курс 2 блок 3 задача)
            Column("course", Text), #название курса !web, python, gamedev, frontend, backend, analytics
            Column('points', Integer), #кол-во баллов !не ограничено
            Column("answer", Text), #ответ (см. answer.md)
            Column("condition", Text), #условие (текст)
            )

photos = Table("photos", metadata, \
            Column("photo_id", Integer, primary_key=True, unique=True, autoincrement=True), #номер фото
            Column("link", Text)) #ссылка на фото

documents = Table("documents", metadata, \
            Column("document_id", Integer, primary_key=True, unique=True, autoincrement=True), #номер файла
            Column("link", Text)) #ссылка на файл
            
# ТАБЛИЦА СТАТУСОВ
statuses = Table("statuses", metadata, \
            Column("status_id", Integer, primary_key=True, unique=True, autoincrement=True), #номер статуса
            Column("task_id", Integer), #номер задания
            Column("student_id", Integer), #номер студента
            Column('status_date', Date), #дата первой отправки
            Column('delivery_status', Boolean), #статус доставки (ОК/ошибка)
            Column("ready_status", Boolean), #статус готовности (готово/не готово)
            Column("reason", Text), #причина ошибки доставки (см. error.md)
            Column('archived', Boolean) #архивирован ли? !если готово - автоархив
            )

# ТАБЛИЦА РЕПОРТОВ
reports = Table("reports", metadata, \
            Column("report_id", Integer, primary_key=True, unique=True, autoincrement=True), #номер репорта
            Column("task_id", Integer), #номер задания
            Column("student_id", Integer), #номер студента
            Column('report_date', Date), #дата отправки
            Column('report_status', Boolean), #статус репорта (решено/не решено)
            Column('reason', Text), #причина репорта (см. error.md)
            Column('archived', Boolean) #архивирован ли? !если решено - автоархив
            )

metadata.create_all(engine)