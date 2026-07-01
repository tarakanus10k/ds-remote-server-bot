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
    duration: float

    def combined_output(self) -> str:
        parts: list[str] = []
        if self.stderr:
            parts.append(self.stderr)
        if self.stdout:
            parts.append(self.stdout)
        return "\n".join(parts).strip()

class COMMAND_EXECUTE:
    def __init__(self, ssh_client: SSH_CONNECT, cfg: CONFIG) -> None:
        self._ssh = ssh_client
        self._cfg = cfg

    def execute(self, command: str, timeout: Optional[int] = None) -> COMMAND_RESULT:
        effective_timeout = timeout or self._cfg.ssh_timeout
        start = time.monotonic()

        with self._ssh.lock:
            if self._ssh.client is None:
                self._ssh.connect()

            client = self._ssh.client
            assert client is not None

            try:
                result = self._exec_locked(client, command, effective_timeout)
            except (paramiko.SSHException, EOFError, socket.error) as e:
                # need make logging system
                self._ssh.connect()
                client = self._ssh.client
                assert client is not None
                result = self._exec_locked(client, command, effective_timeout)

        duration = time.monotonic() - start
        result.duration = duration
        return result
    
    def _exec_locked(self, client: paramiko.SSHClient, command: str, timeout: int) -> COMMAND_RESULT:
        channel = client.get_transport().open_session()
        channel.settimeout(timeout)
        try:
            channel.exec_command(command)
        except paramiko.SSHException as e:
            channel.close()
            raise e
        
        stdout_buf = bytearray()
        stderr_buf = bytearray()

        try:
            while not channel.exit_status_ready():
                if channel.recv_ready():
                    stdout_buf.extend(channel.recv(4096))
                if channel.recv_stderr_ready():
                    stderr_buf.extend(channel.recv_stderr(4096))
                if not (channel.recv_ready() or channel.recv_stderr_ready()):
                    time.sleep(0.02)
        except socket.timeout:
            # need make logging system
            pass
        finally:
            channel.close()

        return COMMAND_RESULT(
            command=command,
            stdout=stdout_buf.decode("utf-8"),
            stderr=stderr_buf.decode("utf-8"),
            duration=0.0
        )