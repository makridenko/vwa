# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    CONTENT = b'<a href="https://github.com/makridenko">its me, Alex!</a>'

    def do_GET(self):
        self.send_response(code=200, message='Hello')
        self.send_header('Content-Type','text/html')
        self.send_header('Content-Length', str(len(self.CONTENT)))
        self.end_headers()
        self.wfile.write(self.CONTENT)
