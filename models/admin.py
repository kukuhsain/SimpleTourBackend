from google.appengine.ext import ndb
from utils.password_hashing import PasswordHashing
from utils.token_hashing import TokenHashing


class Admin(ndb.Model):
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    session = ndb.BooleanProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def _check_email_availability(cls, email):
        if cls._get_admin_by_email(email):
            return False
        else:
            return True

    @classmethod
    def _get_admin_by_email(cls, email):
        return cls.query(cls.email == email).get()

    @classmethod
    def register(cls, email, password):
        if cls._check_email_availability(email):
            hashed_password = PasswordHashing.make_hashing_password(email, password)
            admin = cls(email=email, password=hashed_password, session=False)
            admin.put()
            return admin.key.id()
        else:
            return False

    @classmethod
    def login(cls, email, password):
        admin = cls._get_admin_by_email(email)
        if admin:
            password_validation_result = PasswordHashing.validate_password(email, password, admin.password)
            if password_validation_result:
                admin.session = True
                admin.put()
                return admin
            else:
                return False
        else:
            return False

    @classmethod
    def logout(cls, admin):
        admin.session = False
        admin.put()
