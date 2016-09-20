import json
from base_controller import Handlers
from models import *

class UserRegister(Handlers):
	def post(self):
		email = self.request.get("email")
		password = self.request.get("password")

		self.response.headers['Content-Type'] = 'application/json'
		if email and password:
			userid = User.register(username, password, email)
			if userid:
				response = {
					"status": "success",
					"message": "Successfully registering a new user"
				}
				self.response.out.write(json.dumps(response))
			else:
				response = {
					"status": "fail",
					"message": "Username is not available"
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

		userid = User.login(username, password)
		self.response.headers['Content-Type'] = 'application/json'
		if userid:
			response = {
				"status": "success",
				"message": "Login Successfully"
			}
			self.response.out.write(json.dumps(response))
		else:
			response = {
				"status": "fail",
				"message": "Login failed, wrong username and/or password"
			}
			self.response.out.write(json.dumps(response))

class UserLogout(Handlers):
	def post(self):
		User.logout()
