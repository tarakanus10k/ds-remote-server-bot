# ------------------------------------------------------------------
# 
# ------------------------------------------------------------------

import discord
from discord.ext import commands

from config import SETTINGS
from cogs.remote_shell import SHELLCOG

# def CREATE_BOT():
#     intents = discord.Intents.default()
#     intents.message_content = True

#     bot = commands.Bot(command_prefix=CONFIG.COMMAND_PREFIX, intents=intents)

#     @bot.event
#     async def on_ready():
#         await bot.load_extension("bot.commands.execute")

#     return bot

class START_BOT(commands.Bot):
    def __init__(self, settings: SETTINGS) -> None:
        intents = discord.Intents.default()
        intents.message_content = True

        super.__init__(
            COMMAND_PREFIX = commands.when_mentioned_or(settings.COMMAND_PREFIX),
            intents = intents,
            help_command = commands.DefaultHelpCommand(),
        )

    async def setup_hook(self) -> None:
        await self.load_extension("bot.cogs.shell")

        synced = await self.tree.sync()

    async def close(self) -> None:
        await super().close()

    async def __aenter__(self) -> START_BOT:
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()