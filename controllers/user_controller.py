from base_controller import Handlers
from models import *

class UserRegister(Handlers):
	def get(self):
		self.render("admin/admin-register.html")

	def post(self):
		username = self.request.get('admin-username')
		password = self.request.get('admin-password')
		password_again = self.request.get('admin-password-again')
		email = self.request.get('admin-email')
		secret_password = self.request.get('admin-secret-password')

		if username and password and password_again and email and secret_password:
			if password != password_again:
				error = "Password should be same with Password Again"
				self.render("admin/admin-register.html", error=error)
			elif secret_password != Credentials.SECRET_PASSWORD:
				error = "You've just inputed a wrong secret password"
				self.render("admin/admin-register.html", error=error)
			else:
				adminid = Admin.register(username, password, email)
				if adminid:
					success = "Successfully registering a new admin"
					self.render("admin/admin-register.html", success=success)
				else:
					error = "Username is not available"
					self.render("admin/admin-register.html", error=error)
		else:
			error = "You must fill all inputs of the form"
			self.render("admin/admin-register.html", error=error)


class UserLogin(Handlers):
	def get(self):
		userid = self.read_secure_cookie('aid')
		if userid:
			self.redirect('/admin/setting')
		else:
			self.render("admin/admin-login.html")

	def post(self):
		username = self.request.get('email')
		password = self.request.get('password')

		userid = Admin.login(username, password)
		if userid:
			self.set_secure_cookie('aid', userid)
			self.redirect('/admin/setting')
		else:
			error = "Login failed, wrong username and/or password"
			self.render("admin/admin-login.html", error=error)

class UserLogout(Handlers):
	def get(self):
		self.set_secure_cookie('aid', '')
		self.redirect('/')

	def post(self):
		self.set_secure_cookie('aid', '')
		self.redirect('/')
