from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
from calculator import eval_expr

class CalcHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/' or parsed.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            with open('index.html', 'rb') as f:
                self.wfile.write(f.read())
        elif parsed.path == '/calc':
            params = parse_qs(parsed.query)
            expr = params.get('expr', [''])[0]
            try:
                result = eval_expr(expr)
                response = {'result': result}
                self.send_response(200)
            except Exception as e:
                response = {'error': str(e)}
                self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, *args):
        pass  # silence default logging

def run(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, CalcHandler)
    print(f'Server running on http://localhost:{port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
