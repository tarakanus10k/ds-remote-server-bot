import discord
from discord.ext import commands

import asyncio

from settings.config import CONFIG
from ssh.ssh_connect import SSH_CONNECT

intents = discord.Intents.default()
intents.message_content = True

class SSH_BOT(commands.Bot):
    def __init__(self, cfg: CONFIG, ssh_conn: SSH_CONNECT) -> None:
        super().__init__(

            command_prefix=commands.when_mentioned_or(cfg.command_prefix),
            intents=intents,
            help_command=commands.DefaultHelpCommand()

        )
        self.cfg = cfg
        self.ssh = ssh_conn

    async def setup_hook(self) -> None:
        await asyncio.get_event_loop().run_in_executor(None, self.ssh.connect)

async def main() -> None:
    ssh = SSH_CONNECT(CONFIG)
    bot = SSH_BOT(CONFIG, ssh)

    token = CONFIG.bot_token

    async with bot:
        await bot.start(token)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass