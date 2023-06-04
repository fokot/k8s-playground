from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

class CustomHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/secret':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            system_variable = os.getenv('ENV_VARIABLE')
            if system_variable:
                message = f"The value of ENV_VARIABLE is: {system_variable}"
            else:
                message = "No value found for ENV_VARIABLE"
            self.wfile.write(message.encode())
        else:
            # Serve files from the local directory
            super().do_GET()

def run_server():
    host = '0.0.0.0'
    port = 8080
    server_address = (host, port)
    httpd = HTTPServer(server_address, CustomHandler)
    print(f"Server started on {host}:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
