import discord
from discord.ext import commands

from settings.config import CONFIG
from ssh.ssh_execute import COMMAND_EXECUTE

class EXECUTOR(commands.Cog):
    def __init__(self, bot: commands.Bot, cfg: CONFIG, ssh_exec: COMMAND_EXECUTE) -> None:
        self.bot = bot
        self.cfg = cfg
        self.ssh = ssh_exec

    @commands.command(name="exec", help="send command to remote server")
    async def exec(self, ctx: commands.Context, *, command_text: str) -> None:
        if ctx.author.bot:
            return
            
        await self._handle_command(ctx, command_text)

    async def _handle_command(self, ctx: commands.Context, command: str) -> None:
        async with ctx.typing():
            result = await self.bot.loop.run_in_executor(None, lambda: self.ssh.execute(command))

            output = result.combined_output