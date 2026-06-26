# ------------------------------------------------------------------
# Typed settings loaded from env vars
# ------------------------------------------------------------------

import os
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path

@dataclass(frozen=True)
class SETTINGS:

    # discord bot
    BOT_TOKEN: str
    COMMAND_PREFIX: str

    # ssh settings
    SSH_HOST: str
    SSH_PORT: int
    SSH_USER: str
    SSH_PASSWORD: str

    @classmethod
    def from_env(cls) -> SETTINGS:
        return cls(

            BOT_TOKEN = os.getenv("BOT_TOKEN"),
            COMMAND_PREFIX = os.getenv("COMMAND_PREFIX", "!"),
            SSH_HOST = os.getenv("SSH_HOST"),
            SSH_PORT = int(os.getenv("SSH_PORT", "22")),
            SSH_USER = os.getenv("SSH_USER"),
            SSH_PASSWORD = os.getenv("SSH_PASSWORD"),

        )
    
def _load_dotenv() -> None:
    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(env_path, override=False)