import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import weather_preprocessing

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7353852762:AAGUVVvwLhW_h_OUPuHWz2kj0nVAiisgUvQ")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Введите адрес для определения погоды:")

@dp.message()
async def handle_address(message: types.Message):
    user_id = message.from_user.id
    user_address = message.text
    logging.info(f"Пользователь {user_id} ввел адрес: {user_address}")
    
    weather_preprocessing.process_address(user_address)
    ans = weather_preprocessing.json_parsing()
    await message.reply(ans)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())