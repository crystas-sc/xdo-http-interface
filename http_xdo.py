#!/usr/bin/env python
"""
Very simple HTTP server in python interfacing with xdotool

"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib
import subprocess
import os
import datetime


class S(BaseHTTPRequestHandler):

	def _set_headers(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

	def _html(self, content):
		return content.encode("utf8")  # NOTE: must return a bytes object!

	def do_GET(self):
		self._set_headers()
		key =""
		cmd =""
		if "?" in self.path:
			queryParams = self.transformQueryParam()
			key = queryParams["key"]
			cmd =  queryParams["cmd"]
			reqTimestamp =  int(queryParams["timestamp"])
			currTimestamp =  datetime.datetime.now().replace(tzinfo = datetime.timezone.utc).timestamp()
			print("timestamp diff ")
			print((int(currTimestamp) - int(reqTimestamp/1000)))
			if int(currTimestamp) - int(reqTimestamp/1000) < 3 :
				print("xdotool "+cmd +" "+ key)
				subprocess.call("xdotool "+cmd +" "+ key, shell=True)
			
		#self.wfile.write(self.getHtmlContent()%{"cmd":cmd, "key":key})
		formattedString = self.getHtmlContent()
		formattedString = formattedString.replace("%(cmd)s", cmd).replace("%(key)s", key)
		self.wfile.write(self._html(formattedString))
		

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

