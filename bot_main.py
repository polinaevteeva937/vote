from aiogram import Bot, Dispatcher, executor
from handlers import register_handlers
# import database_main
from sensitive import token

bot = Bot(token=token)
dp = Dispatcher(bot)

register_handlers(dp) 
executor.start_polling(dp, skip_updates=True)