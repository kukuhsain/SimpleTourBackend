import json
from base_controller import Handlers
from models.destination import Destination


class DestinationAdd(Handlers):
    def post(self):
        admin = self._authenticate_admin()
        if admin:
            title = self.request.get("title")
            content = self.request.get("content")
            location = self.request.get("location")
            image = self.request.get("image")

            destination = Destination.add(title, content, location, image)
            response = {
                "destination": {
                    "destination_id": destination.key.id(),
                    "title": destination.title,
                    "content": destination.content,
                    "location": destination.location,
                    "image_url": "/image?image_id=" + destination.image_id,
                    "created_date": destination.created_date.isoformat(),
                }
            }
            self._response_json(response)


class DestinationGetAll(Handlers):
    def get(self):
        destinations = Destination.get_all()
        list_of_json_destinations = []
        for destination in destinations:
            list_of_json_destinations.append({
                "destination_id": destination.key.id(),
                "title": destination.title,
                "content": destination.content,
                "location": destination.location,
                "image_url": "/image?image_id=" + destination.image_id,
                "created_date": destination.created_date.isoformat(),
            })
        response = {
            "destinations": list_of_json_destinations,
        }
        self._response_json(response)


class DestinationUpdate(Handlers):
    def post(self, user_key):
        admin = self._authenticate_admin()
        if admin:
            destination_id = self.request.get("destination_id")
            title = self.request.get("title")
            content = self.request.get("content")
            location = self.request.get("location")

            destination = Destination.update(destination_id, title, content, location)
            if destination:
                response = {
                    "destination": {
                        "destination_id": destination.key.id(),
                        "title": destination.title,
                        "content": destination.content,
                        "location": destination.location,
                        "image_url": "/image?image_id=" + destination.image_id,
                        "created_date": destination.created_date.isoformat(),
                    }
                }
                self._response_json(response)
            else:
                self._raise_500_response()

class DestinationDelete(Handlers):
    def post(self, user_key):
        admin = self._authenticate_admin()
        if admin:
            destination_id = self.request.get("destination_id")
            result = Destination.delete(destination_id)
            if result:
                response = {
                    "status": "success",
                    "message": "Delete destination successfully",
                }
                self._response_json(response)
            else:
                self._raise_500_response()
