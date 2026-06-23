# команда !exec для запуска на сервере

import discord
from discord.ext import commands
from config import CONFIG
from ssh.executor import RUN_REMOTE_COMMAND

class EXECUTE_COMMAND(commands.cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="exec")
    async def execute_command(self, ctx: commands.Context, *, command: str):

        msg: str

        try:
            output = await RUN_REMOTE_COMMAND(command)
        except Exception as e:
            await msg.adit(f"{e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(EXECUTE_COMMAND(bot))