#!/usr/bin/env python
"""
Very simple HTTP server in python interfacing with xdotool

"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib
import subprocess
import os
import datetime
import ssl
import os
from pathlib import Path
import cgi
import shutil


class S(BaseHTTPRequestHandler):
	base_static_file_path = os.path.dirname(os.path.abspath(__file__))+'/static_files'
	upload_file_path = os.path.dirname(os.path.abspath(__file__))+'/static_files/uploads'
	
	def _set_headers(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

	def _html(self, content):
		return content.encode("utf8")  # NOTE: must return a bytes object!

	def get_static_file_list(self, path):
		files = []
		relative_path = path.replace(self.base_static_file_path, "").strip()
		if Path(path).is_dir() and path != self.base_static_file_path:
			dir_list = relative_path.split("/")
			print(f"dir_list {dir_list}")
			files.append("/"+"/".join(dir_list[:-1]))
		files = files + [os.path.join(relative_path, cur_path) for cur_path in os.listdir(path)]
		return [f"<li><a href='/fileserve/{file}'>{file}</a></li>" for file in files ]

	def do_GET(self):
		print("Request url {}".format(self.path))
		
		if "/fileserve" in self.path:
			path = self.path
			file_path = urllib.parse.unquote(path.replace("/fileserve","").strip()).split("/")
			list_path = self.base_static_file_path
			if file_path :
				abs_file_path = os.path.join(self.base_static_file_path, *file_path)
				if Path(abs_file_path).is_dir() :
					list_path = os.path.join(self.base_static_file_path, *file_path)
				elif Path(abs_file_path).is_file() :
					self.send_response(200)
					self.send_header("Content-type", "application/octet")
					self.end_headers()
					with open(abs_file_path, 'rb') as infile:
						d = infile.read(1024)
						while d:
							self.wfile.write(d)
							d = infile.read(1024)
					return
			print(f"file_path {file_path} base_static_file_path {self.base_static_file_path} list_path {list_path}")
			
			file_list_response = "<html><ul>"+''.join(self.get_static_file_list(list_path))+"</ul></html>" 
			self._set_headers()
			self.wfile.write(self._html(file_list_response))
			
			self.send_response(200)
			return

		self._set_headers()
		key =""
		cmd =""
		if "?" in self.path:
			queryParams = self.transformQueryParam()
			key = queryParams["key"] if "key" in queryParams.keys() else key 
			cmd = queryParams["cmd"] if "cmd" in queryParams.keys() else cmd 
			reqTimestamp =  int(queryParams["timestamp"])
			currTimestamp =  datetime.datetime.now().replace(tzinfo = datetime.timezone.utc).timestamp()
			print("timestamp diff ")
			print((int(currTimestamp) - int(reqTimestamp/1000)))
			with open('run_commands.csv', 'a',  encoding='utf8') as writer:
				writeLine = f"{cmd} {key},{reqTimestamp}\n"
				writer.write(writeLine)
			if int(currTimestamp) - int(reqTimestamp/1000) < 3 :
				print("xdotool "+cmd +" "+ key)
				subprocess.call("xdotool "+cmd +" "+ key, shell=True)
			
		#self.wfile.write(self.getHtmlContent()%{"cmd":cmd, "key":key})
		formatted_string = self.getHtmlContent().replace("%(cmd)s", cmd).replace("%(key)s", key)
		self.wfile.write(self._html(formatted_string))
		

	def do_HEAD(self):
		self._set_headers()


	def do_POST(self):
		if self.path == '/fileupload':
			form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],
                         })
			filename = form['file'].filename
			with open(os.path.join(self.upload_file_path,filename), 'wb') as fh:
				shutil.copyfileobj(form['file'].file, fh)
		self.send_response(301)
		self.send_header('Location','/fileserve/uploads')
		self.end_headers()

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
			   
			    
				   
def run(server_class=HTTPServer, handler_class=S, addr="0.0.0.0", port=443):
	# server_address = (addr, port)
	# httpd = server_class(server_address, handler_class)

	# print(f"Starting httpd server on {addr}:{port}")
	# httpd.serve_forever()

	server_address = (addr, port)
	httpd = HTTPServer(server_address, handler_class)
	httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True, certfile='./certificate.crt', keyfile="./privatekey.key", ssl_version=ssl.PROTOCOL_TLS)
	print(f"Starting httpd server on {addr}:{port}")
	httpd.serve_forever()


if __name__ == "__main__":
	run()

