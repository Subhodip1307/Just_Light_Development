from .settings import template_folder
from jinja2 import Environment, FileSystemLoader

class Template:
    def __init__(self, templates_dir=template_folder):
        self.routes = {}
        print(templates_dir)
        self.env = Environment(loader=FileSystemLoader(templates_dir))


    def render(self,filename,context:dict={}):
        template=self.env.get_template(filename)
        return template.render(**context)


