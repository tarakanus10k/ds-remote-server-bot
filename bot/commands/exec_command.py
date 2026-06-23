# команда !exec для запуска на сервере

import discord
from discord.ext import commands
from config import CONFIG
from ssh.executor import RUN_REMOTE_COMMAND

class EXECUTE_COMMAND(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="exec")
    async def execute_command(self, ctx: commands.Context, *, command: str):
        try:
            output = await RUN_REMOTE_COMMAND(command)
            await ctx.send(f"```\n{output}\n```")
        except Exception as e:
            await ctx.send(f"Error: {e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(EXECUTE_COMMAND(bot))