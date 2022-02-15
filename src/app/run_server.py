# -*- coding: utf-8 -*-

from http.server import HTTPServer

from lib.api_gen import RequestHandler


def run_server() -> None:
    server_address = ('', 8080)
    server = HTTPServer(
        server_address=server_address, 
        RequestHandlerClass=RequestHandler,
    )
    server.serve_forever()
