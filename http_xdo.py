#!/usr/bin/env python
"""
Very simple HTTP server in python interfacing with xdotool

"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib
import subprocess
import os


class S(BaseHTTPRequestHandler):
	htmlContent = """
	<html>
		<body>
			<form id=form method=get >
				<p>Last command: %(cmd)s %(key)s </p>
				
				<input type=text name="cmd" value="%(cmd)s" />
				<input type=text name="key" value="%(key)s" />
				<button type=submit >submit</button>
				<br/>
				<div style="display=flex">
				<button type=button onClick="btnClickKey('--clearmodifiers XF86AudioRaiseVolume')" > Vol+</button>
				<button type=button onClick="btnClickKey('--clearmodifiers XF86AudioLowerVolume')" > Vol-</button>
				
				<button type=button onClick="btnClickKey('alt+Tab')" > alt+Tab</button>
				<button type=button onClick="btnClickKey('alt+F4')" > alt+F4</button>
				<button type=button onClick="btnClickMouse(' 0 0 click 1')" > Left Click</button>
				<button type=button onClick="btnClickMouse(' 0 0 click 3')" > Right Click</button>
				<button type=button onClick="btnClickSetCmd('mousemove_relative --sync ')" > Mouse Move</button>
				<button type=button onClick="btnClickSetCmd('key')" > key cmd</button>
				
				<button type=button onClick="btnClickKey('--clearmodifiers XF86AudioMute')" > Mute</button>
				<button type=button onClick="btnClickKey('--clearmodifiers XF86AudioPlay')" > Play</button>
				<button type=button onClick="btnClickKey('--clearmodifiers XF86AudioStop')" > Stop</button>
				<button type=button onClick="btnClickKey('--clearmodifiers XF86AudioPrev')" > Prev</button>
				<button type=button onClick="btnClickKey('--clearmodifiers XF86AudioNext')" > Next</button>


				</div>
				
				<script>
				var form = document.getElementById("form");
				function btnClickKey(value){
					form.cmd.value= "key";
					form.key.value=value;
					form.submit();
				}
				function btnClickMouse(value){
					form.cmd.value= "mousemove_relative --sync ";
					form.key.value=value;
					form.submit();
				}
				function btnClickSetCmd(cmd){
					form.cmd.value= cmd;
					form.key.value="";
				}
				</script>
				<style>
					button{
					min-height:70px;
					min-width:100px;
					margin:10px
					
					}
				</style>
			</form>
		</body>
	</html>
	"""
	
	def _set_headers(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

	def _html(self, message):
		"""This just generates an HTML document that includes `message`
		in the body. Override, or re-write this do do more interesting stuff.
		"""
		content = f"<html><body><h1>{message}</h1></body></html>"
		return content.encode("utf8")  # NOTE: must return a bytes object!

	def do_GET(self):
		self._set_headers()
		key =""
		cmd =""
		if "?" in self.path:
			queryParams = self.transformQueryParam()
			key = queryParams["key"]
			cmd =  queryParams["cmd"]
			subprocess.call("xdotool "+cmd +" "+ key, shell=True)
			
		#self.wfile.write(self._html(self.htmlContent%{"cmd":cmd, "key":key}))
		#self.wfile.write(self.getHtmlContent()%{"cmd":cmd, "key":key})
		self.wfile.write(self._html(self.getHtmlContent()))
		

	def do_HEAD(self):
		self._set_headers()


	def do_POST(self):
		# Doesn't do anything with posted data
		self._set_headers()
		self.wfile.write(self._html("POST!"))

	def transformQueryParam(self):
		print(self.path)
		queryString = self.path.split("?")[1]
		queryParams = {item[0]: item[1] for item in urllib.parse.parse_qsl(queryString)}
		#queryContent = queryString.split("&")
		#queryParamsArray = [item.split("=") for item in queryContent]
		#queryParamsArray = [urllib.parse.parse_qs(item) for item in queryContent]
		#queryParams = {item[0]:item[1] for item in queryParamsArray}
		print(queryParams)
		return queryParams
		
	def getHtmlContent(self):
		fName = "xdo_input.html"
		if os.path.exists(fName):
			with open(fName, 'r') as f:
				try:
				   html = f.read()
				   #print(html)
				   return html
				except IOError as e:
					print("IO Error")
			   
			    
				   
def run(server_class=HTTPServer, handler_class=S, addr="0.0.0.0", port=80):
	server_address = (addr, port)
	httpd = server_class(server_address, handler_class)

	print(f"Starting httpd server on {addr}:{port}")
	httpd.serve_forever()


if __name__ == "__main__":
	run()
