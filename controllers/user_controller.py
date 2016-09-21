import json
from base_controller import Handlers
from models import *

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
				response = {
					"status": "fail",
					"message": "Email is not available"
				}
				self.response.out.write(json.dumps(response))
		else:
			error = ""
			response = {
				"status": "fail",
				"message": "You must fill all inputs of the form"
			}
			self.response.out.write(json.dumps(response))

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
			response = {
				"status": "fail",
				"message": "Login failed, wrong email and/or password"
			}
			self.response.set_status(401, message="Unauthenticated... wrong email and/or password")
			self.response.out.write(json.dumps(response))

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
			response = {
				"status": "fail",
				"message": "Logout failed"
			}
			self.response.set_status(403, message="Forbidden")
			self.response.out.write(json.dumps(response))
