import http.server
import os

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=r"D:\作业\EnglishLearn", **kwargs)

    def log_message(self, format, *args):
        pass

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

if __name__ == '__main__':
    server = http.server.HTTPServer(('127.0.0.1', 8081), Handler)
    print("English server: http://127.0.0.1:8081")
    server.serve_forever()
