import os
import jinja2
def load_template(name):
    path = os.path.join('app/templates/', name)
    with open(os.path.abspath(path), 'r') as fp:
        return jinja2.Template(fp.read())