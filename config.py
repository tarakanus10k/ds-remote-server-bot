import os
from dotenv import load_dotenv

load_dotenv()

class CONFIG:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    SSH_HOST = os.getenv("SSH_HOST")
    SSH_PORT = int(os.getenv("SSH_PORT"))
    SSH_USER = os.getenv("SSH_USER")
    SSH_PASSWORD = os.getenv("SSH_PASSWORD")
    COMMAND_PREFIX = os.getenv("COMMAND_PREFIX")