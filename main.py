
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import random

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Объект бота. Вставьте сюда свой токен
bot = Bot(token="6671029563:AAEU1OjipMJrfN1n6eFJoKBSoZsYl2JxgX4")

# Диспетчер
dp = Dispatcher()

v1 = ""
v2 = ""

@dp.message(Command("start"))
async def cmd_start(message):
    global v1, v2
    v1 = ""
    v2 = ""
    await message.answer("Введите первый вариант")

@dp.message(F.text)
async def handler(message: types.Message):
    global v1, v2
    if v1 == "":                                                                    
        v1 = message.text
        await message.answer("Введите второй вариант")
    elif v2 == "":
        v2 = message.text
        await message.answer(random.choice([v1, v2])) #/dice

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())