from google.appengine.ext import ndb
from utils.password_hashing import PasswordHashing
from utils.token_hashing import TokenHashing


class Destination(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def add(cls, user, title, content):
        parent = user.key
        destination = cls(parent=parent, title=title, content=content)
        destination.put()
        return destination

    @classmethod
    def get_all_by_specific_user(cls, user):
        ancestor = user.key
        destinations = cls.query(ancestor=ancestor).fetch()
        return destinations

    @classmethod
    def get_some_by_specific_user(cls, user, amount):
        ancestor = user.key
        destinations = cls.query(ancestor=ancestor).fetch(amount)
        return destinations

    @classmethod
    def update(cls, user, destination_id, title, content):
        destination = cls.get_by_id(int(destination_id))
        if destination:
            destination.title = title
            destination.content = content
            destination.put()
            return destination
        else:
            return False

    @classmethod
    def delete(cls, destination_id):
        destination = cls.get_by_id(int(destination_id))
        if destination:
            destination.key.delete()
            return True
        else:
            return False
