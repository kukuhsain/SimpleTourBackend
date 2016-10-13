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
                    "createdDate": destination.created_date.isoformat(),
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
                "createdDate": destination.created_date.isoformat(),
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
            image = self.request.get("image")

            destination = Destination.update(destination_id, title, content, location, image)
            if destination_id:
                response = {
                    "status": "success",
                    "message": "Update destination successfully",
                }
                self._response_json(response)
            else:
                self.response.set_status(403, message="Forbidden")

class DestinationDelete(Handlers):
    def post(self, user_key):
        admin = self._authenticate_admin()
        if admin:
            destination_id = self.request.get("destination_id")

            destination_id = Destination.delete(destination_id)
            if destination_id:
                response = {
                    "status": "success",
                    "message": "Delete destination successfully",
                }
                self._response_json(response)
            else:
                self.response.set_status(403, message="Forbidden")
