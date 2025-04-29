import asyncio
from urllib.parse import parse_qs
from .request import Request

class JustLightDevelopment:
    def __init__(self):
        self.routes = {}

    def route(self, path):
        def decorator(func):
            self.routes[path] = func
            return func
        return decorator

    async def __call__(self, scope, receive, send):
        assert scope['type'] == 'http'
        body = b''
        more_body = True
        while more_body:
            message = await receive()
            body += message.get('body', b'')
            more_body = message.get('more_body', False)
        request = Request(scope, body)

        handler = self.routes.get(request.path)
        if handler:
            response_body = await handler(request)
            await send({
                'type': 'http.response.start',
                'status': 200,
                'headers': [(b'content-type', b'text/html')],
            })
            await send({
                'type': 'http.response.body',
                'body': response_body.encode(),
            })
        else:
            await send({
                'type': 'http.response.start',
                'status': 404,
                'headers': [(b'content-type', b'text/plain')],
            })
            await send({
                'type': 'http.response.body',
                'body': b'Not Found',
            })