from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

# модели валидации
class User(BaseModel):
    username: str
    password: str

class Student(BaseModel):
    chat_id: int
    register_date: date
    name: str
    age: date
    phone: str
    course: str
    points: int
    archived: bool

class Student_edit(BaseModel):
    chat_id: int
    name: Optional[str] = None
    age: Optional[date] = None
    phone: Optional[str] = None
    course: Optional[str] = None
    points: Optional[int] = None
    archived: Optional[bool] = None