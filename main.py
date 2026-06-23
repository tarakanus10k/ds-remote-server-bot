# точка входа, запуск бота

import asyncio
from bot.client import CREATE_BOT
from config import CONFIG

async def main():
    bot = CREATE_BOT()
    await bot.start(CONFIG.DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())