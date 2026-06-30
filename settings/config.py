import os
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv()

@dataclass
class CONFIG:

    # discord data
    bot_token: str = field(default_factory=lambda: os.getenv("BOT_TOKEN"))
    command_prefix: str = field(default_factory=lambda: os.getenv("COMMAND_PREFIX", "!"))

    # ssh data
    ssh_host: str = field(default_factory=lambda: os.getenv("SSH_HOST"))
    ssh_port: int = field(default_factory=lambda: int(os.getenv("SSH_PORT", "22")))
    ssh_username: str = field(default_factory=lambda: os.getenv("SSH_USERNAME"))
    ssh_password: str = field(default_factory=lambda: os.getenv("SSH_PASSWORD"))
    ssh_key_path: str = field(default_factory=lambda: os.getenv("SSH_KEY_PATH"))
    ssh_passphrase: str = field(default_factory=lambda: os.getenv("SSH_PASSPHRASE"))

config = CONFIG()