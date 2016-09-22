import webapp2
from functools import wraps
from utils.token_hashing import TokenHashing
from models.user import User
import json

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
		access_token = self.request.get("access_token")
		user_id = TokenHashing().check_secure_value(access_token)
		print user_id
		if user_id:
			self.user = User.get_by_id(int(user_id))
			print self.user
			if self.user:
				if self.user.session:
					f(self)
				else:
					response = {
						"status": "fail",
						"message": "Forbidden"
					}
					self.response.set_status(403, message="Forbidden")
					self.response.out.write(json.dumps(response))
			else:
				response = {
					"status": "fail",
					"message": "Forbidden"
				}
				self.response.set_status(403, message="Forbidden")
				self.response.out.write(json.dumps(response))
		else:
			response = {
				"status": "fail",
				"message": "Forbidden"
			}
			self.response.set_status(403, message="Forbidden")
			self.response.out.write(json.dumps(response))
	return wrapper
