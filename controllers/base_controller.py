import webapp2
from functools import wraps
from utils.token_hashing import TokenHashing
from models.user import User
import json


class Handlers(webapp2.RequestHandler):
    def _raise_401_response(self, description="Failed Authentication"):
        response = {
            "error": {
                "code": "unauthorized",
                "description": description,
            }
        }
        self.response.set_status(401)
        self.response.out.write(json.dumps(response))

    def _raise_403_response(self, description="Forbidden"):
        response = {
            "error": {
                "code": "forbidden",
                "description": description,
            }
        }
        self.response.set_status(403)
        self.response.out.write(json.dumps(response))

    def _raise_404_response(self, description="Not Found"):
        response = {
            "error": {
                "code": "not found",
                "description": description,
            }
        }
        self.response.set_status(404)
        self.response.out.write(json.dumps(response))

    def _raise_500_response(self, description="Internal Server Error"):
        response = {
            "error": {
                "code": "server error",
                "description": description,
            }
        }
        self.response.set_status(500)
        self.response.out.write(json.dumps(response))


def authenticate_user(f):
    @wraps(f)
    def wrapper(self):
        access_token = self.request.get("access_token")
        print access_token
        user_id = TokenHashing.check_secure_value(access_token)
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
