import webapp2
from controllers import *

app = webapp2.WSGIApplication([
	('/', Home),
	# User Section
	('/user/register', UserRegister),
	('/user/login', UserLogin),
	('/user/logout', UserLogout),

	('/destination/add', DestinationAdd),
	('/destination/getall', DestinationGetAll),
	('/destination/getsome', DestinationGetSome),
	('/destination/update', DestinationUpdate),
	('/destination/delete', DestinationDelete),
	], debug=True)
