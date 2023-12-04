"""МОДЕЛИ ТАБЛИЦ РАЗДЕЛА КОВОДСТВО"""
"""ШИФР РАЗДЕЛА - cov"""

from sqlalchemy import Table, Column, MetaData, select, insert, update, delete, create_engine
from sqlalchemy.types import Integer, Float, Text, Date, DateTime, Boolean
from database_main import engine
metadata = MetaData()

compendium = Table("compendium", metadata, \
            Column("compendium_id", Integer, primary_key=True, unique=True, autoincrement=True), #номер студента
            Column("course", Text), #номер чата
            Column("link", Text), #дата регистрации
            Column('archived', Boolean) #в архиве?
            )

records = Table("records", metadata, \
            Column("record_id", Integer, primary_key=True, unique=True, autoincrement=True), #номер студента
            Column("course", Text), #номер чата
            Column("link", Text), #дата регистрации
            Column('archived', Boolean) #в архиве?
            )

tests = Table("tests", metadata, \
            Column("test_id", Integer, primary_key=True, unique=True, autoincrement=True), #номер студента
            Column("course", Text), #номер чата
            Column("link", Text), #дата регистрации
            Column('archived', Boolean) #в архиве?
            )

metadata.create_all(engine)