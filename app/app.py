import falcon
import mongoengine as mongo
from .settings import MONGO
from app.resources.RegisterResource import RegisterResource
from app.resources.LoginResource import LoginResource
from app.resources.UsersResource import UsersResource
from app.resources.DashboardResource import DashboardResource

app = application = falcon.App(media_type='text/html',cors_enable=True)

users = UsersResource()
dashboard = DashboardResource()
register = RegisterResource()
login = LoginResource()

app.add_route('/login', login)
app.add_route('/signup', register)
app.add_route('/users', users)
app.add_route('/dashboard', dashboard)

mongo.connect(
    MONGO['DATABASE'],
    host = MONGO['HOST'],
    port = MONGO['PORT'],
    username = MONGO['USERNAME'],
    password = MONGO['PASSWORD']
)