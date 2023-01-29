from http.server import HTTPServer , BaseHTTPRequestHandler
content = '''
 <!DOCTYPE html>
<html>
<head>
<title>simple web browser</title>
</head>
<body>
   <h1> Welocome</h1>
</body>
</html>
'''

class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print('request recived')
        self.send_response(200)
        self.send_header("content-type","text/html;charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8080)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()        