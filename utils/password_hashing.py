import hashlib
import random
from string import letters


class PasswordHashing:
    @classmethod
    def make_salt(cls, length=5):
        return ''.join(random.choice(letters) for x in xrange(length))

    @classmethod
    def make_hashing_password(cls, name, password, salt=None):
        if not salt:
            salt = cls.make_salt()
            print 'salt: '+salt
        h = hashlib.sha256(str(name)+str(password)+str(salt)).hexdigest()
        return '%s,%s' % (salt, h)
    
    @classmethod
    def validate_password(cls, name, password, h):
        salt = h.split(',')[0]
        return h == cls.make_hashing_password(name, password, salt)
