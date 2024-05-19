from aiogram import Bot, Dispatcher

from config import bot_api

from handlers import router as handlers_router
from functions import router as functions_router
from callback_query import router as callback_router

bot = Bot(token=bot_api)
dp = Dispatcher()

dp.include_router(handlers_router)
dp.include_router(functions_router)
dp.include_router(callback_router)

print('bot is running...')

if __name__ == "__main__":
    dp.run_polling(bot)
