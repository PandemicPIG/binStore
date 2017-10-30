import json

def execute(handler):
  handler.send_response(200)
  
  handler.send_header("Content-type", "application/json")
  handler.send_header("Set-Cookie", "test=myCookie")
  handler.end_headers()
  
  handler.wfile.write(json.dumps({
    'path': handler.path,
    'req': handler.post_data
  }))
  
def create(handler):
  pass

def insert(handler):
  pass

def delete(handler):
  pass