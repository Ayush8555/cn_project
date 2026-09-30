from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json, sys, hashlib, socket

NAME = sys.argv[1]
PORT = int(sys.argv[2])

class H(BaseHTTPRequestHandler):
    def send(self, code, body=b"", ctype="application/json", extra=None):
        self.send_response(code)
        self.send_header("X-Backend", NAME)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if body:
            self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self.send(200, f"<h1>Backend {NAME} is running</h1>".encode(), "text/html")
        elif self.path == "/api/status":
            body = json.dumps({"backend": NAME, "status": "ok"}).encode()
            self.send(200, body, extra={"Cache-Control": "no-store"})
        elif self.path == "/api/cached":
            body = json.dumps({"message": "cacheable content"}).encode()
            etag = '"' + hashlib.md5(body).hexdigest() + '"'
            extra = {"Cache-Control": "max-age=60", "ETag": etag}
            if self.headers.get("If-None-Match") == etag:
                self.send(304, b"", extra=extra)
            else:
                self.send(200, body, extra=extra)
        else:
            self.send(404, b'{"error":"not found"}')

class Server(ThreadingHTTPServer):
    address_family = socket.AF_INET6   # dual-stack listen on "::"

Server(("::", PORT), H).serve_forever()
