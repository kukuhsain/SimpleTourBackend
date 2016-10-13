import json

from controllers.base_controller import Handlers
from models.admin import Admin
from utils.token_hashing import TokenHashing


class AdminRegister(Handlers):
    def post(self):
        email = self.request.get("email")
        password = self.request.get("password")

        if email and password:
            userid = Admin.register(email, password)
            if userid:
                response = {
                    "status": "success",
                    "message": "Successfully registering a new user"
                }
                self.response.out.write(json.dumps(response))
            else:
                self._raise_500_response("Email is not available")
        else:
            self._raise_500_response("You must fill all inputs of the form")


class AdminLogin(Handlers):
    def post(self):
        email = self.request.get("email")
        password = self.request.get("password")

        admin = Admin.login(email, password)
        if admin:
            response = {
                "status": "success",
                "message": "Login Successfully",
                "access_token": TokenHashing.make_secure_value(str(admin.key.id())),
            }
            self._response_json(response)
        else:
            self._raise_401_response("Login failed, wrong email and/or password")


class AdminLogout(Handlers):
    def post(self):
        admin = self._authenticate_admin()
        if admin:
            Admin.logout(admin)
            response = {
                "status": "success",
                "message": "Logout Successfully",
            }
            self._response_json(response)
