import webapp2
from controllers import *

app = webapp2.WSGIApplication([
	('/', Home),
	# User Section
	('/user/register', UserRegister),
	('/user/login', UserLogin),
	('/user/logout', UserLogout),
	], debug=True)
