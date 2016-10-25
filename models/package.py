from google.appengine.ext import ndb

from models.image_model import ImageModel


class Package(ndb.Model):
    destination_id = ndb.IntegerProperty()
    title = ndb.StringProperty()
    content = ndb.TextProperty()
    location = ndb.StringProperty()
    image_id = ndb.IntegerProperty()
    price = ndb.FloatProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)
    updated_date = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def add(cls, destination_id, title, content, location, image, price):
        package = cls(destination_id=int(destination_id), title=title, content=content, location=location)
        if image:
            image_model = ImageModel.add(image)
            package.image_id = image_model.key.id()
        try:
            package.price = float(price)
        except ValueError:
            pass
        package.put()
        return package

    @classmethod
    def get_all_by_destination_id(cls, destination_id):
        packages = cls.query(cls.destination_id == int(destination_id)).fetch()
        return packages

    @classmethod
    def update(cls, destination_id, package_id, title, content, location, price):
        package = cls.get_by_id(int(package_id))
        if package:
            if package.destination_id == int(destination_id):
                package.title = title
                package.content = content
                package.location = location
                try:
                    package.price = float(price)
                except ValueError:
                    pass
                package.put()
                return package
            else:
                return False
        else:
            return False

    @classmethod
    def delete(cls, destination_id, package_id):
        package = cls.get_by_id(int(package_id))
        if package:
            if package.destination_id == int(destination_id):
                package.key.delete()
                return True
            else:
                return False
        else:
            return False
