import os
import falcon
import jinja2
import uuid
from app.models.user import User
from .helpers import load_template
import bcrypt

class UsersResource:
  def on_get(self,req,res):
    form = req.media
    try:
      result = User.objects.get(email=form["email"])
      if bcrypt.checkpw(form['password'], result.password):
        res.set_cookie('session', resul.email)
        raise falcon.HTTPMovedPermanently('/login')
    except:
      raise falcon.HTTPMovedPermanently('/login')

  def on_post(self, req, res):
    form = req.media
    pass_bytes = form['password'].encode('utf-8')
    salt = bcrypt.gensalt(10)
    hashed = bcrypt.hashpw(pass_bytes, salt)

    new_user = User(uuid=str(uuid.uuid4()),email=form['email'],password=hashed)
    new_user.save()

    res.set_cookie("session", new_user.uuid)

    res.status = falcon.HTTP_201
    raise falcon.HTTPMovedPermanently('/dashboard')