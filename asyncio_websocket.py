#websocket
import asyncio
from websockets import serve
import ssl
import subprocess
import mouse
import re


ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_cert = "./certificate.crt"
ssl_key = "./privatekey.key"

ssl_context.load_cert_chain(ssl_cert, keyfile=ssl_key)

async def echo(websocket):
    async for message in websocket:
        print(message)
        if "mousemove_relative" in message and "click" not in message and "mousedown" not in message :
            # if "click" in message :
            #     clk = message.split("click ")[1]
            #     print(f"clk {clk}")
            #     if clk == "1" :
            #        print("click left")
            #        mouse.click(button='left')
            #     elif clk == "3" :
            #        mouse.right_click()
            #     elif clk == "4" :
            #        mouse.wheel(delta=1)
            #     elif clk == "5" :
            #        mouse.wheel(delta=-1)
            #     continue

		
            mv = message.split("sync ")[1].split(" ")
            # print(f"mv {mv}")
            mouse.move(int(float(mv[0])),int(float(mv[1])),absolute=False)
            continue
			
        try:
            # print("subprocess")
            if(message.startswith("type ")):
                # with open('string_file.txt', "w") as myfile:
                #     myfile.write(" ".join(message.split(" ")[1:]))
                # subprocess.call("cat string_file.txt | xargs xdotool type ", shell=True, timeout=0.1)
                cmd_str_arr = message.split(" ")[1:]
                arr_len = len(cmd_str_arr)
                for i in range(arr_len):
                    subprocess.call("xdotool type "+ re.sub(r"('|\")",'\\\1',cmd_str_arr[i]), shell=True, timeout=0.1)
                    if i != arr_len-1:
                        subprocess.call("xdotool key space", shell=True, timeout=0.1)
                
            else:    
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
