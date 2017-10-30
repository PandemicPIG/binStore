import json
import BaseHTTPServer
from src import data

PORT = 8700
server_address = ('', PORT)

class request_handler(BaseHTTPServer.BaseHTTPRequestHandler):

  def do_POST(self):
    content_len = int(self.headers.getheader('content-length', 0))
    self.post_data = json.loads(self.rfile.read(content_len))
    
    self.call_endpoint(self.path)
    
  def call_endpoint(self, path):
    if path[-1:] == '/': path = path[:-1]
      
    if path == '/select': data.select(self)
    elif path == '/create': data.create(self)
    elif path == '/insert': data.insert(self)
    elif path == '/delete': data.delete(self)
    else:
      status = 404
      self.send_response(status)
      self.send_header("Content-type", "application/json")
      self.end_headers()

      self.wfile.write(json.dumps({
        'status': status,
        'error': 'page not found'
      }))

server = BaseHTTPServer.HTTPServer(server_address, request_handler)
server.serve_forever()
