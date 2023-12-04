"""МОДЕЛИ ТАБЛИЦ РАЗДЕЛА КОДИУМ"""
"""ШИФР РАЗДЕЛА - cod"""

from sqlalchemy import Table, Column, MetaData, select, insert, update, delete, create_engine
from sqlalchemy.types import Integer, Float, Text, Date, DateTime, Boolean
from database_main import engine
metadata = MetaData()

typicals = Table("typicals", metadata, \
            Column("typical_id", Integer, primary_key=True, unique=True, autoincrement=True), #номер студента
            Column("course", Text), #номер чата
            Column("link", Text), #дата регистрации
            Column('archived', Boolean) #в архиве?
            )

speedruns = Table("students", metadata, \
            Column("speedrun_id", Integer, primary_key=True, unique=True, autoincrement=True), #номер студента
            Column("course", Text), #номер чата
            Column("link", Text), #дата регистрации
            Column('archived', Boolean) #в архиве?
            )

metadata.create_all(engine)