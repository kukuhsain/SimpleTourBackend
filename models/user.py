from google.appengine.ext import ndb

class User(ndb.Model):
	username = ndb.StringProperty(required=True)
	password = ndb.StringProperty(required=True)
	email = ndb.StringProperty()
	created_date = ndb.DateTimeProperty(auto_now_add=True)

	@classmethod
	def get_user_by_username(cls, username):
		user = cls.query(cls.username==username).get()
		print user
		return user

	@classmethod
	def register(cls, username, password, email=None):
		user = cls.get_user_by_username(username)
		if not user:
			hashed_password = HashingPassword().make_hashing_password(username, password)
			new_admin = cls(username=username, password=hashed_password, email=email)
			new_admin.put()
			return new_admin.key.id()
		else:
			return False

	@classmethod
	def login(cls, username, password):
		user = cls.get_user_by_username(username)
		if user:
			password_validation_result = HashingPassword().validate_password(username, password, user.password)
			if password_validation_result:
				return user.key.id()
			else:
				return False
		else:
			return False
