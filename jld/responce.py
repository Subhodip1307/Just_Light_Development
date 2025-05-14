import json

class HTMLResponse:
    def __init__(self, content, status=200):
        self.content:str = content.encode()
        self.status = status
        self.headers = [(b'content-type', b'text/html')]

class JSONResponse:
    def __init__(self, data, status=200):
        self.content = json.dumps(data).encode()
        self.status = status
        self.headers = [(b'content-type', b'application/json')]

class HTTPResponse(HTMLResponse):...