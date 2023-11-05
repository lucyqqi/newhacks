import http.server
import socketserver
import subprocess
from urllib.parse import urlparse, parse_qs
import json



class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))

        # Update the 'urls.txt' file with the received data
        with open('urls.txt', 'w') as urllist:
            urllist.write('\n'.join(data))

        try:
            subprocess.run(["python", "amazon.py"])
            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps({'message': 'Data received and processed successfully'}).encode())
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())

        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps({'message': 'Data received and processed successfully'}).encode())

if __name__ == "__main__":
    PORT = 8080  # Choose a port for your server
    with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()