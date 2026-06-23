 # функция выполнения команды на сервере

import asyncio
from ssh.connection import GET_SSH_CLIENT, CONNECT

async def RUN_REMOTE_COMMAND(command: str):
    client = GET_SSH_CLIENT()

    try:
        await asyncio.to_thread(CONNECT, client)
        stdin, stdout, stderr = await asyncio.to_thread(client.exec_command, command, timeout=30)

        out = await asyncio.to_thread(stdout.read)
        err = await asyncio.to_thread(stderr.read)
        exit_status = stdout.channel.recv_exit_status()
        result = out.decode("utf-8", errors="replace")

        if err:
            result += "\n[STDERR]\n" + err.decode("utf-8", errors="replace")
        if exit_status != 0:
            result += f"\n[Код возврата: {exit_status}]"
        return result.strip()
    
    except Exception as e:
        raise

    finally:
        client.close()