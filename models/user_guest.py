from google.appengine.ext import ndb
from utils.password_hashing import PasswordHashing
from utils.token_hashing import TokenHashing


class UserGuest(ndb.Model):
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    name = ndb.StringProperty()
    phone = ndb.StringProperty()
    image_url = ndb.StringProperty()
    session = ndb.BooleanProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def _check_email_availability(cls, email):
        if cls._get_user_by_email(email):
            return False
        else:
            return True

    @classmethod
    def _get_user_by_email(cls, email):
        return cls.query(cls.email == email).get()

    @classmethod
    def register(cls, email, password, name, phone):
        if cls._check_email_availability(email):
            hashed_password = PasswordHashing.make_hashing_password(email, password)
            user = cls(email=email, password=hashed_password, name=name, phone=phone, session=True)
            user.put()
            return user
        else:
            return False

    @classmethod
    def login(cls, email, password):
        user = cls._get_user_by_email(email)
        if user:
            password_validation_result = PasswordHashing.validate_password(email, password, user.password)
            if password_validation_result:
                user.session = True
                user.put()
                return user
            else:
                return False
        else:
            return False

    @classmethod
    def update_profile(cls, access_token, name, phone):
        user = cls.get_by_id(user_id)
        if user:
            user.name = name
            user.phone = phone
        else:
            False

    @classmethod
    def logout(cls, access_token):
        user_id = TokenHashing.check_secure_value(access_token)
        if user_id:
            user = cls.get_by_id(user_id)
            if user:
                user.session = False
                user.put()
                return True
            else:
                return False
        else:
            return False
