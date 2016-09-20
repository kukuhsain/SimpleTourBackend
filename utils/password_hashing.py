import hashlib
import random
from string import letters

class PasswordHashing():
	def make_salt(self, length=5):
		return ''.join(random.choice(letters) for x in xrange(length))

	def make_hashing_password(self, name, password, salt=None):
		if not salt:
			salt = self.make_salt()
			print 'salt: '+salt
		h = hashlib.sha256(str(name)+str(password)+str(salt)).hexdigest()
		return '%s,%s' % (salt, h)

	def validate_password(self, name, password, h):
		salt = h.split(',')[0]
		return h == self.make_hashing_password(name, password, salt)
