import webapp2
import json

from functools import wraps

from models.admin import Admin
from utils.token_hashing import TokenHashing
from models.user_guest import UserGuest


class Handlers(webapp2.RequestHandler):
    def _response_json(self, dict_response):
        self.response.headers["Content-Type"] = "application/json"
        self.response.out.write(json.dumps(dict_response))

    def _response_image(self, image):
        self.response.headers["Content-Type"] = "image/*"
        self.response.out.write(image)

    def _raise_401_response(self, description="Failed Authentication"):
        response = {
            "error": {
                "code": "unauthorized",
                "description": description,
            }
        }
        self.response.set_status(401)
        self._response_json(response)

    def _raise_403_response(self, description="Forbidden"):
        response = {
            "error": {
                "code": "forbidden",
                "description": description,
            }
        }
        self.response.set_status(403)
        self._response_json(response)

    def _raise_404_response(self, description="Not Found"):
        response = {
            "error": {
                "code": "not found",
                "description": description,
            }
        }
        self.response.set_status(404)
        self._response_json(response)

    def _raise_500_response(self, description="Internal Server Error"):
        response = {
            "error": {
                "code": "server error",
                "description": description,
            }
        }
        self.response.set_status(500)
        self._response_json(response)

    def _authenticate_admin(self):
        access_token = self.request.get("access_token")
        admin_id = TokenHashing.check_secure_value(access_token)
        if admin_id:
            admin = Admin.get_by_id(int(admin_id))
            if admin.session:
                return admin
            else:
                self._raise_403_response()
                return False
        else:
            self._raise_403_response()
            return False

    def _authenticate_user_guest(self):
        access_token = self.request.get("access_token")
        user_id = TokenHashing.check_secure_value(access_token)
        if user_id:
            user = UserGuest.get_by_id(int(user_id))
            if user.session:
                return user
            else:
                self._raise_403_response()
                return False
        else:
            self._raise_403_response()
            return False