import falcon
from app.models.user import User
from .helpers import load_template

class DashboardResource:
  def on_get(self,req,res):
    try:
      cookies = req.cookies
      session = cookies['session']
    except:
      raise falcon.HTTPMovedPermanently('/signup')
    
    template = load_template('dashboard.html')
    users_data = User.objects

    res.status = falcon.HTTP_200
    res.body = template.render(users=users_data)