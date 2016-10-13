from google.appengine.ext import ndb
from utils.password_hashing import PasswordHashing
from utils.token_hashing import TokenHashing


class Destination(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    location = ndb.StringProperty()
    image = ndb.BlobProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)
    updated_date = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def add(cls, title, content, location, image):
        if not image:
            image = None
        destination = cls(title=title, content=content, location=location, image=image)
        destination.put()
        return destination

    @classmethod
    def get_all(cls):
        destinations = cls.query().fetch()
        return destinations

    @classmethod
    def update(cls, destination_id, title, content, location, image):
        destination = cls.get_by_id(int(destination_id))
        if not image:
            image = None
        if destination:
            destination.title = title
            destination.content = content
            destination.location = location
            destination.image = image
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
