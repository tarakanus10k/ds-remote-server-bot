import discord
from discord.ext import commands

from config import SETTINGS
from ...ssh.executor import EXECUTE_CONNECTION

class SHELLCOG(commands.Cog):
    def __init__(self, bot: commands.Bot, client: EXECUTE_CONNECTION):
        self.bot = bot

    async def _execute(self, ctx: commands.Context, *, command: str) -> None:
        try:
            result = await self.client.exec(command)
        except Exception as e:
            raise
        
    @commands.command(name="exec", help="run !exec to send message on server")
    async def run_prefix(self, ctx: commands.Context, *, command: str) -> None:
        await ctx.typing()
        await self._execute(ctx, command, timeout=float(self.settings.default_timeout))