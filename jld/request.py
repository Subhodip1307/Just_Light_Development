from urllib.parse import parse_qs

class BaseMethod:
    def __init__(self,data={}):
        self.data:dict=data

    def __repr__(self)->dict:
        return repr(self.data)
    
    def get(self,key)->str:
        return self.data.get(key)[0]
    def getlist(self,key)->str:
        return self.data.get(key)


class GET(BaseMethod):...
class POST(BaseMethod):...
# class PUT(BaseMethod):...
# class OPTIONS(BaseMethod):...



class Request:
    def __init__(self, scope, body: bytes):
        self.method = scope['method']
        self.path = scope['path']
        self.headers = dict(scope['headers'])
        self.GET:BaseMethod = GET()
        self.POST:BaseMethod = POST()
        if self.method == "GET" or self.method == "POST":
            self.GET = GET(parse_qs(scope.get("query_string", b"").decode()))
            self.POST = POST(parse_qs(body.decode()))
        
            
        
            


  
