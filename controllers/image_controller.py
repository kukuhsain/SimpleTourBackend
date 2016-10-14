from base_controller import Handlers
from models.image_model import ImageModel


class ImageGet(Handlers):
    def get(self):
        image_id = self.request.get("image_id")
        if image_id.isdigit():
            image_model = ImageModel.get(image_id)
            if image_model:
                self._response_image(image_model.image)
            else:
                self._raise_500_response()
        else:
            self._raise_500_response()

