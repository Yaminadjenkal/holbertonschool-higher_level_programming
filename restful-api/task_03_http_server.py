#!/usr/bin/python3
'''
This module contains a simple HTTP server for GET requests
'''
import http.server
import json


class SimpleHandler(http.server.BaseHTTPRequestHandler):
    """Handles HTTP GET requests"""
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            response_data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            response_info = {
                            "version": "1.0",
                            "description":
                            "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-type", "application.json")
            self.end_headers()
            self.wfile.write(json.dumps(response_info).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


httpd = http.server.HTTPServer(('localhost', 8000), SimpleHandler)
print("Server running")
httpd.serve_forever()
