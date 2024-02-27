from http.server import HTTPServer, BaseHTTPRequestHandler

HOST, PORT = '192.168.0.105', 9999
body = '''
<html>
  <body>
    <h1>HELLO WORLD!</h1>
    Как у тебя дела?
  </body>
</html>
'''

class MyHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes(body, 'UTF-8'))


server = HTTPServer((HOST, PORT), MyHTTP)
print('Server ran...')

server.serve_forever()
server.server_close()
print('Server stopped')
