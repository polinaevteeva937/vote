import admin.pydantic.pyd_acc as pyd_acc
import admin.pydantic.pyd_cod as pyd_cod
import admin.pydantic.pyd_com as pyd_com
import admin.pydantic.pyd_cou as pyd_cou
import admin.pydantic.pyd_cov as pyd_cov
import admin.pydantic.pyd_gen as pyd_gen
import admin.pydantic.pyd_mag as pyd_mag
import admin.pydantic.pyd_mar as pyd_mar
import admin.pydantic.pyd_web as pyd_web

import admin.requests.req_acc as req_acc
import admin.requests.req_cod as req_cod
import admin.requests.req_com as req_com
import admin.requests.req_cou as req_cou
import admin.requests.req_mag as req_mag
import admin.requests.req_cov as req_cov
import admin.requests.req_gen as req_gen
import admin.requests.req_mar as req_mar
import admin.requests.req_web as req_web

#from rabbitmq_publish import send_channel

from fastapi import APIRouter
from fastapi.responses import FileResponse
router = APIRouter()

@router.get("/magica/catalog")
async def catalog():
    
    return {'a': 1}

def get_data(course_id=None, block_id=None):
    if block_id is None:
        x = req_mag.course_get(course_id)
    else:
        x = req_mag.block_get(course_id, block_id)
    list_of_dicts = list(map(lambda x: dict(course_id=x[0], block_id=x[1], order_id=x[2], task_id=x[3], course=x[4], points=x[5], answer=x[6], condition=x[7]), x))
    return list_of_dicts

@router.get("/magica/catalog/frontend")
async def catalog_frontend():
    return get_data(1)

@router.get("/magica/catalog/frontend/{block_id}")
async def catalog_frontend_1(block_id: int):
    return get_data(1, block_id)

@router.get("/magica/catalog/backend")
async def catalog_frontend():
    return get_data(2)

@router.get("/magica/catalog/backend/{block_id}")
async def catalog_frontend_1(block_id: int):
    return get_data(2, block_id)

@router.get("/magica/catalog/analytics")
async def catalog_frontend():
    return get_data(3)

@router.get("/magica/catalog/analytics/{block_id}")
async def catalog_frontend_1(block_id: int):
    return get_data(3, block_id)

@router.get("/magica/catalog/data_science")
async def catalog_frontend():
    return get_data(4)

@router.get("/magica/catalog/data_science/{block_id}")
async def catalog_frontend_1(block_id: int):
    return get_data(4, block_id)

@router.put("/magica/catalog/add")
async def magica_catalog_add(homework: pyd_mag.Homework):
    try:
        req_mag.catalog_put(homework)
        return {"answer": "успешно"}
    except Exception as e:
        print(e) 
        return {"answer": "ошибка"}

@router.patch("/magica/catalog/edit")
async def magica_catalog_edit(homework: pyd_mag.Homework):
    try:
        req_mag.catalog_patch(homework)
        return {"answer": "успешно"}
    except Exception as e:
        print(e) 
        return {"answer": "ошибка"}
    
# Отправка домашки ученику в Телеграм
@router.post("/magica/catalog/send")
async def magica_catalog_send(send_homework: pyd_mag.SendHomework):   
    try:        
        return {"answer": "успешно"}
    except Exception as e:
        print(e) 
        return {"answer": "ошибка"}

@router.get("/magica/status")
async def magica_status():
    # получить все статусы из БД (список из кортежей)
    # list_of_tuples = status_get()
    # list_of_dicts = ...
    pass

    # return list_of_dicts

# @router.get("/magica/report")
# async def magica_report():
    
#     return list_of_dicts

# ПРОСМОТР ВСЕХ УЧЕНИКОВ
@router.get("/profile/students")
async def profile_students():
    try:
        students = req_acc.students_get()
        return students
    except Exception as e:
        print(e) 
        return {"answer": "ошибка"}
    
# ПРОСМОТР ОДНОГО УЧЕНИКА
@router.get("/profile/students/{chat_id}")
async def profile_student(chat_id):
    try:
        student = req_acc.student_get(chat_id)
        return student
    except Exception as e:
        print(e) 
        return {"answer": "ошибка"}

# ДОБАВЛЕНИЕ НОВОГО УЧЕНИКА
@router.put("/profile/students/add")
async def profile_students_add(student: pyd_acc.Student):
    try:
        req_acc.students_put(student.chat_id, student.register_date, student.name, \
                             student.age, student.phone, student.course, student.points, \
                             student.archived)
        return {"answer": "успешно"}
    except Exception as e:
        print(e) 
        return {"answer": "ошибка"}

# ИЗМЕНЕНИЕ СУЩЕСТВУЮЩЕГО УЧЕНИКА
@router.patch("/profile/students/edit")
async def profile_students_edit(student_edit: pyd_acc.Student_edit):
    try:
        req_acc.students_patch(student_edit.chat_id, student_edit.name, student_edit.age, student_edit.phone, \
                               student_edit.course, student_edit.points, student_edit.archived)
        return {"answer": "успешно"}
    except Exception as e:
        print(e) 
        return {"answer": "ошибка"}

# УДАЛЕНИЕ УЧЕНИКА
@router.delete("/profile/students/remove")
async def profile_stugents_remove(student_edit: pyd_acc.Student_edit):
    try:
        req_acc.students_delete(student_edit.chat_id)
        return {"answer": "успешно"}
    except Exception as e:
        print(e) 
        return {"answer": "ошибка"}

# @router.post("/profile/students/send")
# async def profile_students_send():
    
#     return {'a': 1}

# @router.get("/profile/students/sort")
# async def profile_students_sort():
    
#     return list_of_dicts

# @router.get("/profile/portfolio")
# async def profile_portfolio():
    
#     return list_of_dicts

# @router.put("/profile/portfolio/add")
# async def profile_portfolio_add():
    
#     return {'a': 1}

# @router.patch("/profile/portfolio/edit")
# async def profile_portfolio_edit():
    
#     return {'a': 1}

# @router.delete("/profile/portfolio/delete")
# async def profile_portfolio_delete():
    
#     return {'a': 1}

# @router.get("/profile/progress")
# async def profile_progress():
    
#     return list_of_dicts

@router.post("/profile/progress/{chat_id}")
async def profile_progress(chat_id):
    file_location = f'./analytics/plots/plt_{chat_id}.png'
    
    return FileResponse(path= file_location, media_type='image/png')

# @router.get("/profile/achievements")
# async def profile_achievements():
    
#     return list_of_dicts

# @router.put("/profile/achievements/add")
# async def profile_achievements_add():
    
#     return {'a': 1}

# @router.patch("/profile/achievements/edit")
# async def profile_achievements_edit():
    
#     return {'a': 1}

# @router.delete("/profile/achievements/remove")
# async def profile_achievements_remove():
    
#     return {'a': 1}

# @router.get("/profile/certificates")
# async def profile_certificates():
    
#     return {'a': 1}

# @router.put("/profile/certificates/add")
# async def profile_certificates_add():
    
#     return {'a': 1}

# @router.patch("/profile/certificates/edit")
# async def profile_certificates_edit():
    
#     return {'a': 1}

# @router.delete("/profile/certificates/remove")
# async def profile_certificates_remove():
    
#     return {'a': 1}

