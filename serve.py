import os
import argparse
import requests
from http.server import HTTPServer, SimpleHTTPRequestHandler

from io import BytesIO

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        print(self.headers)
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())
        requests.post(url='http://35.231.132.43:8083/submit',
                        files=body
                        )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", default=8000, type=int, help="port to listen on")
    args = parser.parse_args()

    os.chdir('static')
    server_address = ('', args.port)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print('serving at http://127.0.0.1:%d' % args.port)
    httpd.serve_forever()


main()
