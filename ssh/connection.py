# менеджер SSH-подключений

import paramiko
from config import CONFIG

def GET_SSH_CLIENT():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return client

def CONNECT(client: paramiko.SSHClient):
    connection_data = {
        "hostname": CONFIG.SSH_HOST,
        "port": CONFIG.SSH_PORT,
        "username": CONFIG.SSH_USER,
        "timeout": 10,
        "password": CONFIG.SSH_PASSWORD,
    }

    client.connect(**connection_data)