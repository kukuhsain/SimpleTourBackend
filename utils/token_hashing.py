import hmac
from configs.credential import TOKEN_SECRET


class TokenHashing:
    @classmethod
    def hash_str(cls, s):
        return hmac.new(TOKEN_SECRET, s).hexdigest()
    
    @classmethod
    def make_secure_value(cls, s):
        return "%s|%s" % (s, cls.hash_str(s))

    @classmethod
    def check_secure_value(cls, s):
        value = s.split('|')[0]
        if s == cls.make_secure_value(value):
            return value
        else:
            return False
