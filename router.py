import webapp2

from controllers.admin_controller import AdminRegister, AdminLogin, AdminLogout
from controllers.destination_controller import DestinationAdd, DestinationUpdate, DestinationDelete
from controllers.destination_controller import DestinationGetAll
from controllers.home_controller import Home
from controllers.user_controller import UserLogin
from controllers.user_controller import UserRegister, UserLogout


app = webapp2.WSGIApplication([
    ('/', Home),

    # Admin Section
    ('/admin/register', AdminRegister),
    ('/admin/login', AdminLogin),
    ('/admin/logout', AdminLogout),

    # User Section
    ('/user/register', UserRegister),
    ('/user/login', UserLogin),
    ('/user/logout', UserLogout),

    ('/destination/add', DestinationAdd),
    ('/destinations', DestinationGetAll),
    ('/destination/update', DestinationUpdate),
    ('/destination/delete', DestinationDelete),
    ], debug=True)
