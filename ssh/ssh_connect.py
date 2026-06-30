import paramiko
import socket
import time
import threading
from typing import Optional

from settings.config import CONFIG
from ssh.ssh_connection_error import SSH_CONNECTION_ERROR

class SSH_CONNECT:
    def __init__(self, cfg: CONFIG) -> None:
        self._cfg = cfg
        self._client = Optional[paramiko.SSHClient] = None
        self._lock = threading.Lock()

    @property
    def lock(self) -> threading.Lock:
        return self._lock
    
    @property
    def client(self) -> Optional[paramiko.SSHClient]:
        return self._client

    def connect(self) -> None:
        with self._lock:
            self._connect_locked()

    def _connect_locked(self) -> None:
        if self._client is not None:
            try:
                self._client.close()
            except Exception:
                pass

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        connect_kwargs: dict = {

            "hostname": self._cfg.ssh_host,
            "port": self._cfg.ssh_port,
            "username": self._cfg.ssh_username,
            "key_filename": self._cfg.ssh_key_path,
            "passphrase": self._cfg.ssh_passphrase,
            "timeout": 10,
            "allow_agent": False,
            "look_for_keys": False

        }

        try:
            client.connect(**connect_kwargs)
        except paramiko.AuthenticationException as e:
            raise SSH_CONNECTION_ERROR(f"{e}") from e
        except paramiko.SSHException as e:
            raise SSH_CONNECTION_ERROR(f"{e}") from e
        except socket.error as e:
            raise SSH_CONNECTION_ERROR(f"e") from e