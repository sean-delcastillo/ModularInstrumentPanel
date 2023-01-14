from jinja2 import (
    Environment, 
    PackageLoader, 
    select_autoescape
)
from datetime import datetime

def render_template(devices: object, is_test: bool) -> str:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    env = Environment(
        loader=PackageLoader("mips"),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True
    )
    template = env.get_template("sketch_template.j2")

    return template.render(devices=devices, 
        test=is_test,
        datetime=dt_string
    )

def save_render(rendered_template: str, profile_name: str):
    with open(f"sketches/{profile_name}.ino", "w") as sketch:
        sketch.write(rendered_template)