import paramiko
import socket
import time
import threading
from dataclasses import dataclass
from typing import Optional

from settings.config import CONFIG
from ssh.ssh_connect import SSH_CONNECT

@dataclass
class COMMAND_RESULT:
    command: str
    stdout: str
    stderr: str

class COMMAND_EXECUTE:
    def __init__(self, ssh_client: SSH_CONNECT, cfg: CONFIG) -> None:
        self._ssh = ssh_client
        self._cfg = cfg

    def execute(self, command: str, timeout: Optional[int] = None) -> None:
        with self._ssh.lock:
            if self._ssh.client is None:
                self._ssh.connect()

            client = self._ssh.client
            assert client is not None

            # create command executing