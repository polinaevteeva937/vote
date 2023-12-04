from sensitive import host, port, user, password, dbname

import sqlalchemy
from sqlalchemy import Table, Column, MetaData, select, insert, update, delete, create_engine
from sqlalchemy.types import Integer, Float, Text, Date, DateTime
from sqlalchemy.orm import sessionmaker
import psycopg2

conn = psycopg2.connect(
    host=host,
    port=port,
    sslmode="verify-full",
    dbname=dbname,
    user=user,
    password=password,
    target_session_attrs="read-write"
)

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}')
Session = sessionmaker(engine)

def complete(query):
    with Session() as session:
        try:
            result = session.execute(query)
            session.commit()
            return result 
        except Exception as e:
            session.rollback()
            print(e)
            print('Изменения в БД откачены') 
        finally:
            session.close()