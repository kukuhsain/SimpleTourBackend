import hmac

class HashingCookie():
	def hash_str(self, s):
		return hmac.new(Credentials.SECRET_COOKIE, s).hexdigest()

	def make_secure_value(self, s):
		return "%s|%s" % (s, self.hash_str(s))

	def check_secure_value(self, s):
		value = s.split('|')[0]
		if s == self.make_secure_value(value):
			return value
		else:
			return False
