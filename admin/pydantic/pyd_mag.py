from pydantic import BaseModel

class Homework(BaseModel): 
    course_id: int
    block_id: int
    order_id: int
    points: int
    answer: str
    condition: str

class SendHomework(BaseModel):
    chat_id: int
    task_id: int