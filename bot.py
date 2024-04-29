import asyncio

from aiogram import Bot, Dispatcher

from handlers import group_games


async def main():
    bot = Bot(token="6671029563:AAEU1OjipMJrfN1n6eFJoKBSoZsYl2JxgX4")
    dp = Dispatcher()

    dp.include_router(group_games.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())