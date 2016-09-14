import webapp2
from functools import wraps

class Handlers(webapp2.RequestHandler):
	def set_secure_cookie(self, name, value):
		if value:
			cookie_value = HashingCookie().make_secure_value(str(value))
		else:
			cookie_value = ''
		self.response.headers.add_header('Set-Cookie', '%s=%s' % (name, cookie_value))

	def read_secure_cookie(self, name):
		cookie_value = self.request.cookies.get(name)
		if cookie_value:
			return HashingCookie().check_secure_value(cookie_value)
		else:
			return False

def authenticate_user(f):
	@wraps(f)
	def wrapper(self):
		adminid = self.read_secure_cookie('uid')
		if adminid:
			f(self)
		else:
			self.redirect('/')
	return wrapper
