from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json
import cgi

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        
    # GET endpoint for /
    def do_GET(self):
        self._set_headers()
        self.wfile.write(bytes(json.dumps({'message': 'Hello from Arden!'}), 'utf-8'))
        
def run(server_class=HTTPServer, handler_class=Server, port=28804):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print(f'Local server blasting off on port {port} 🚀')
    httpd.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
        