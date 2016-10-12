import json
from base_controller import Handlers
from models import User


class UserRegister(Handlers):
    def post(self):
        email = self.request.get("email")
        password = self.request.get("password")

        self.response.headers['Content-Type'] = 'application/json'
        if email and password:
            userid = User.register(email, password)
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


class UserLogin(Handlers):
    def post(self):
        username = self.request.get("email")
        password = self.request.get("password")

        access_token = User.login(username, password)
        self.response.headers['Content-Type'] = 'application/json'
        if access_token:
            response = {
                "status": "success",
                "message": "Login Successfully",
                "access_token": access_token
            }
            self.response.out.write(json.dumps(response))
        else:
            self._raise_401_response("Login failed, wrong email and/or password")


class UserLogout(Handlers):
    def post(self):
        access_token = self.request.get("access_token")
        print access_token
        status = User.logout(access_token)
        self.response.headers['Content-Type'] = 'application/json'
        if status:
            response = {
                "status": "success",
                "message": "Logout Successfully",
            }
            self.response.out.write(json.dumps(response))
        else:
            self._raise_403_response("Logout Failed")
