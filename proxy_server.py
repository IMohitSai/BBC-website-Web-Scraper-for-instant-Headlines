import http.server
import socketserver
import urllib.request

PORT = 8080

class Proxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            url = self.path[1:]  # Remove the leading '/'
            with urllib.request.urlopen(url) as response:
                self.send_response(response.status)
                for key, value in response.getheaders():
                    self.send_header(key, value)
                self.end_headers()
                self.wfile.write(response.read())
        except Exception as e:
            self.send_error(404, str(e))

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Proxy) as httpd:
        print("Serving at port", PORT)
        httpd.serve_forever()
