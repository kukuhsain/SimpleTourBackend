from google.appengine.ext import ndb

from models.image_model import ImageModel
from utils.password_hashing import PasswordHashing
from utils.token_hashing import TokenHashing


class Package(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    location = ndb.StringProperty()
    image_id = ndb.IntegerProperty()
    price = ndb.FloatProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)
    updated_date = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def add(cls, title, content, location, image, price):
        package = cls(title=title, content=content, location=location, price=price)
        if image:
            image_model = ImageModel.add(image)
            package.image_id = image_model.key.id()
        package.put()
        return package

    @classmethod
    def get_all(cls):
        packages = cls.query().fetch()
        return packages

    @classmethod
    def update(cls, package_id, title, content, location, price):
        package = cls.get_by_id(int(package_id))
        if package:
            package.title = title
            package.content = content
            package.location = location
            package.price = price
            package.put()
            return package
        else:
            return False

    @classmethod
    def delete(cls, package_id):
        package = cls.get_by_id(int(package_id))
        if package:
            package.key.delete()
            return True
        else:
            return False
