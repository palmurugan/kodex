import os

from jinja2 import Environment, FileSystemLoader, StrictUndefined


class CodeGenerator:

    def __init__(self):
        # Set the path to the directory containing the template files
        template_dir = os.path.join(os.path.dirname(__file__), '../templates')
        self.env = Environment(loader=FileSystemLoader(template_dir), undefined=StrictUndefined)

    def render(self, template, filename, target_location, context):
        template = self.env.get_template(template)
        print("Printing the value", context["base_dir"])
        with open(target_location / filename, 'w') as f:
            f.write(template.render(context))
