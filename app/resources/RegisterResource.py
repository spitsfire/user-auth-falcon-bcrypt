import falcon
from .helpers import load_template

class RegisterResource:
  def on_get(self,req,res):
    template = load_template('signup.html')

    res.status = falcon.HTTP_200
    res.body = template.render()