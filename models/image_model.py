from google.appengine.ext import ndb


class ImageModel(ndb.Model):
    image = ndb.BlobProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)
    updated_date = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def add(cls, image):
        image_model = cls(image=image)
        image_model.put()
        return image_model

    @classmethod
    def get(cls, image_id):
        image_model = cls.get_by_id(int(image_id))
        if image_model:
            return image_model
        else:
            return False

    @classmethod
    def update(cls, image_id, image):
        image_model = cls.get_by_id(int(image_id))
        if image_model:
            image_model.image = image
            image_model.put()
            return image_model
        else:
            return False

    @classmethod
    def delete(cls, image_id):
        image_model = cls.get_by_id(int(image_id))
        if image_model:
            image_model.key.delete()
            return True
        else:
            return False
