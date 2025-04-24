from urllib.parse import parse_qs

class Request:
    def __init__(self, scope, body: bytes):
        self.method = scope['method']
        self.path = scope['path']
        self.headers = dict(scope['headers'])

        if self.method == "GET":
            self.GET = parse_qs(scope.get("query_string", b"").decode())
            self.POST = {}
        elif self.method == "POST":
            self.GET = {}
            self.POST = parse_qs(body.decode())
        else:
            self.GET = {}
            self.POST = {}
