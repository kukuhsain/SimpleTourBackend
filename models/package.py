from google.appengine.ext import ndb

from models.image_model import ImageModel
from utils.password_hashing import PasswordHashing
from utils.token_hashing import TokenHashing


class Package(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    location = ndb.StringProperty()
    image_id = ndb.IntegerProperty()
    price = ndb.IntegerProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)
    updated_date = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def add(cls, destination, title, content, location, image, price):
        parent = destination.key
        package = cls(parent=parent, title=title, content=content, location=location)
        if image:
            image_model = ImageModel.add(image)
            package.image_id = image_model.key.id()
        if price.isdigit():
            package.price = int(price)
        package.put()
        return package

    @classmethod
    def get_all_by_ancestor(cls, destination):
        ancestor = destination.key
        packages = cls.query(ancestor == ancestor).fetch()
        return packages

    @classmethod
    def update(cls, destination, package_id, title, content, location, price):
        parent = destination.key
        package = cls.get_by_id(int(package_id), parent=parent)
        if package:
            package.title = title
            package.content = content
            package.location = location
            if price.isdigit():
                package.price = int(price)
            package.put()
            return package
        else:
            return False

    @classmethod
    def delete(cls, destination, package_id):
        parent = destination.key
        package = cls.get_by_id(int(package_id), parent=parent)
        if package:
            package.key.delete()
            return True
        else:
            return False
