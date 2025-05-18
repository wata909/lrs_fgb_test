from http.server import SimpleHTTPRequestHandler, HTTPServer
import mimetypes

mimetypes.add_type('application/octet-stream', '.fgb')

class MyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

HTTPServer(('localhost', 8000), MyHandler).serve_forever()

