 # функция выполнения команды на сервере

import asyncio
from ssh_client import SSH_CONNECTION
from dataclasses import dataclass

@dataclass
class STDDATA:
    stdin: str
    stdout: str
    stderr: str

class EXECUTE_CONNECTION:
    async def run_remote_command(command: str):
        client = SSH_CONNECTION.get_ssh_client

        try:
            await asyncio.to_thread(SSH_CONNECTION.connection, client)
            STDDATA.stdin, STDDATA.stdout, STDDATA.stderr = await asyncio.to_thread(client.exec_command, command, timeout=30)

            out = await asyncio.to_thread(STDDATA.stdout.read)
            err = await asyncio.to_thread(STDDATA.stderr.read)
            exit_status = await asyncio.to_thread(STDDATA.stdout.channel.recv_exit_status)
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