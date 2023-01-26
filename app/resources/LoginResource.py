import falcon
from .helpers import load_template

class LoginResource:
  def on_get(self,req,res):
    if "session" in req.cookies:
      raise falcon.HTTPMovedPermanently('/dashboard')
    else:
      template = load_template('index.html')
      res.status = falcon.HTTP_200
      res.body = template.render()