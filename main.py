from aiogram import executor
from config import dp
from handlers import start, call_back
from database.sql_commands import Database
async def onstart_up(_):
    db = Database()
    db.sql_create_tables()


start.register_start_handlers(dp=dp)
call_back.register_callback_handlers(dp=dp)

if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=onstart_up
    )
