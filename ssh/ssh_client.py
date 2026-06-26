import paramiko
import asyncio
from dataclasses import dataclass

from config import SETTINGS

@dataclass
class SSH_CONNECTION:
    hostname: str
    port: int
    username: str
    password: str

    @classmethod
    def from_settings(cls) -> SSH_CONNECTION:
        return cls(

            hostname = SETTINGS.SSH_HOST,
            port = SETTINGS.SSH_PORT,
            username = SETTINGS.SSH_USER,
            password = SETTINGS.SSH_PASSWORD,

        )
    
    def get_ssh_client(self) -> paramiko.SSHClient:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        return client
    
    def connection(self) -> paramiko.SSHClient:
        client = self.get_client()
        client.connect(

            hostname = self.hostname,
            port = self.port,
            username = self.username,
            password = self.password,
        
        )

