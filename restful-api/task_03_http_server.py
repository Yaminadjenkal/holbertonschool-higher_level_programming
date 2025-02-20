from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def _send_response(self, status_code, content_type, content):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        if self.path == '/':
            content = b"Hello, this is a simple API!"
            self._send_response(200, 'text/html', content)

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            content = json.dumps(data).encode()
            self._send_response(200, 'application/json', content)

        elif self.path == '/status':
            status = {"status": "OK"}
            content = json.dumps(status).encode()
            self._send_response(200, 'application/json', content)

        else:
            error_message = {"error": "Endpoint not found"}
            content = json.dumps(error_message).encode()
            self._send_response(404, 'application/json', content)

def run(server_class=HTTPServer, handler_class=MyHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting server at http://localhost:8000")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

