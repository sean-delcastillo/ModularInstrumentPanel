from jinja2 import (
    Environment, 
    PackageLoader, 
    select_autoescape
)

env = Environment(
    loader=PackageLoader("mips"),
    autoescape=select_autoescape()
)

template = env.get_template("sketch_template.j2")

print(template.render(the="variables", go="here"))