import asyncio
from .request import Request

class JustLightDevelopment:
    def __init__(self, templates_dir="templates"):
        self.routes = {}

    def route(self, path, methods=["GET"]):
        def decorator(func):
            for method in methods:
                self.routes[(path, method)] = func
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
        handler = self.routes.get((request.path, request.method))

        if handler:
            response = await handler(request)
            await send({
                'type': 'http.response.start',
                'status': response.status,
                'headers': response.headers,
            })
            await send({
                'type': 'http.response.body',
                'body': response.content,
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
