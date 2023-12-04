from fastapi import FastAPI
import uvicorn
from endpoints import router

from aiogram import Bot, Dispatcher
from handlers import register_handlers

import database_main
from sensitive import token

import asyncio

app = FastAPI()
app.include_router(router)

bot = Bot(token=token)
dp = Dispatcher(bot)

# async def main():
#     # Запускаем FastAPI сервер
#     config = uvicorn.Config(app, host="127.0.0.1", port=8000)
#     server = uvicorn.Server(config)
    
#     # Определяем задачи asyncio
#     register_handlers(dp)
#     polling_task = dp.start_polling()
#     server_task = asyncio.create_task(server.serve())

#     # Асинхронно запускаем задачи
#     await asyncio.gather(polling_task, server_task)

# if __name__ == "__main__":
#     # asyncio.run заменён на это, чтобы избежать проблем с 
#     # "RuntimeWarning: coroutine '...' was never awaited"
#     # В Python >= 3.7:
#     asyncio.run(main())