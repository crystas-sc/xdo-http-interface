#websocket
import asyncio
from websockets import serve
import ssl
import subprocess


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_cert = "./certificate.crt"
ssl_key = "./privatekey.key"

ssl_context.load_cert_chain(ssl_cert, keyfile=ssl_key)

async def echo(websocket):
    async for message in websocket:
        # print(message)
        try:
            subprocess.call("xdotool "+message, shell=True, timeout=0.1)
        except:
            print("command timeout")
        # await websocket.send(message)

async def main():
    print("start websocket")
    async with serve(echo, "0.0.0.0", 8765, ssl=ssl_context):
        print("ws running forever")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
	# asyncio.run(main())
    asyncio.get_event_loop().run_until_complete(main())
