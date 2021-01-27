import socket
import asyncio
from concurrent.futures import ThreadPoolExecutor

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 1234))
s.listen(5)
async def ainput(prompt: str = "") -> str:
    with ThreadPoolExecutor(1, "AsyncInput") as executor:
        return await asyncio.get_event_loop().run_in_executor(executor, input, prompt)      #shoutout to delivrance

async def getmessageandpost():
    clientsocket.send(bytes(await ainput("Message:"),"utf-8")
    print("Your message is succesfully sended!")
async def recievemessages():
    while msg = s.recv(1024) and msg is not None:
        print(msg.decode("utf-8"))                  
async def main():
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established!")
        while True:
            await getmessageandpost()
            await recievemessages()
asyncio.run(main())
