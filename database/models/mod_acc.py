"""МОДЕЛИ ТАБЛИЦ РАЗДЕЛА АККАУНТ"""
"""ШИФР РАЗДЕЛА - acc"""

from sqlalchemy import Table, Column, MetaData, select, insert, update, delete, create_engine
from sqlalchemy.types import Integer, Float, Text, Date, DateTime, Boolean, BigInteger
from database_main import engine
metadata = MetaData()

students = Table("students", metadata, \
            Column("student_id", Integer, autoincrement=True), #номер студента
            Column("chat_id", Integer, primary_key=True, unique=True), #номер чата
            Column("register_date", Date), #дата регистрации
            Column("name", Text), #имя
            Column("age", Date), #дата рождения
            Column("phone", Text), #телефон родителя
            Column("course", Text), #курс
            Column("points", Integer), #баллы на балансе
            Column('archived', Boolean) #в архиве?
            )

# 2 сущности - ученик и достижение
# 2 ученика могут иметь одно и то же достижение
# и 2 достижения могут быть у одного ученика
# если у нас только 2 столбца - achievement_id и student_id
# то ни один из них не подходит для того, чтобы однозначно определить, событие получения достижения
# поэтому мы вводим дополнительно reward_id - который обозначает СОБЫТИЕ получения достижения
# этот reward_id будет уникальным абсолютно у каждого события

progress = Table("progress", metadata, \
            Column("progress_id", BigInteger, primary_key=True), #номер прогресса
            Column("chat_id", BigInteger), #номер чата
            Column("date", DateTime), #дата обновления
            Column("points", BigInteger), #дата обновления
            )

portfolio = Table("portfolio", metadata, \
            Column("project_id", Integer, primary_key=True, unique=True, autoincrement=True), #номер проекта
            Column("chat_id", Integer, unique=True), #номер чата
            Column("link", Text), #ссылка на проект
            )

achievements = Table("achievements", metadata, \
            Column("achievement_id", Integer, primary_key=True, unique=True, autoincrement=True), #номер достижения
            Column("level", Text), #уровень достижения
            Column("description", Text), #описание достижения
            Column("points", Integer), #баллы за достижение
            )

achievements_bind = Table("achievements_bind", metadata, \
            Column("chat_id", Integer), #номер чата
            Column("achievement_id", Integer) #номер достижения
            )

certificates = Table("certificates", metadata, \
            Column("certificate_id", Integer, primary_key=True, unique=True, autoincrement=True), #номер сертификата
            Column("link", Text), #ссылка на сертификат
            Column("description", Text), #описание сертификата
            Column("points", Integer), #баллы за сертификат
            )

certificates_bind = Table("certificates_bind", metadata, \
            Column("chat_id", Integer), #номер чата
            Column("certificate_id", Integer) #номер сертификата
            )

metadata.create_all(engine)