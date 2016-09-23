import webapp2
from functools import wraps
from utils.token_hashing import TokenHashing
from models.user import User
import json

class Handlers(webapp2.RequestHandler):
	def _raise_403_response(self):
		response = {
			"status": "fail",
			"message": "Forbidden"
		}
		self.response.set_status(403, message="Forbidden")
		self.response.out.write(json.dumps(response))

def authenticate_user(f):
	@wraps(f)
	def wrapper(self):
		access_token = self.request.get("access_token")
		print access_token
		user_id = TokenHashing().check_secure_value(access_token)
		print user_id
		if user_id:
			self.user = User.get_by_id(int(user_id))
			print self.user
			if self.user:
				if self.user.session:
					f(self)
				else:
					self._raise_403_response()
			else:
				self._raise_403_response()
		else:
			self._raise_403_response()
	return wrapper
