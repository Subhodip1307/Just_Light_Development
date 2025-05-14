from .settings import template_folder
from jinja2 import Environment, FileSystemLoader
from .responce import HTMLResponse
import asyncio

class Template:
    def __init__(self, templates_dir=template_folder):
        self.env = Environment(loader=FileSystemLoader(templates_dir))


    def render_sync(self,filename,context:dict={}):
        template=self.env.get_template(filename)
        return HTMLResponse(template.render(**context))
    
    async def render(self, filename, context: dict = {}):
        return await asyncio.to_thread(self.render_sync, filename, context)


