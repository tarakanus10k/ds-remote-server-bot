import discord
from discord.ext import commands
from config import CONFIG

def CREATE_BOT():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix=CONFIG.COMMAND_PREFIX, intents=intents)

    @bot.event
    async def on_ready():
        await bot.load_extension("bot.commands.execute")

    return bot