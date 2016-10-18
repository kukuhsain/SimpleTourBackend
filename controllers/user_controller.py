import json
from base_controller import Handlers
from models.user_guest import UserGuest
from utils.token_hashing import TokenHashing


class UserRegister(Handlers):
    def post(self):
        email = self.request.get("email")
        password = self.request.get("password")

        self.response.headers['Content-Type'] = 'application/json'
        if email and password:
            user = UserGuest.register(email, password)
            if user:
                response = {
                    "status": "success",
                    "message": "Successfully registering a new user",
                    "accessToken": TokenHashing.make_secure_value(str(user.key.id()))
                }
                self._response_json(response)
            else:
                self._raise_500_response("Email is not available")
        else:
            self._raise_500_response("You must fill all inputs of the form")


class UserLogin(Handlers):
    def post(self):
        username = self.request.get("email")
        password = self.request.get("password")

        user = UserGuest.login(username, password)
        if user:
            response = {
                "status": "success",
                "message": "Login Successfully",
                "accessToken": TokenHashing.make_secure_value(str(user.key.id()))
            }
            self._response_json(response)
        else:
            self._raise_401_response("Login failed, wrong email and/or password")


class UserLogout(Handlers):
    def post(self):
        access_token = self.request.get("access_token")
        print access_token
        status = UserGuest.logout(access_token)
        if status:
            response = {
                "status": "success",
                "message": "Logout Successfully",
            }
            self._response_json(response)
        else:
            self._raise_403_response("Logout Failed")
