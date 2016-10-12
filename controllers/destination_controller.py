import json
from base_controller import Handlers, authenticate_user
from models import User, Destination


class DestinationAdd(Handlers):
    @authenticate_user
    def post(self):
        access_token = self.request.get("access_token")
        title = self.request.get("title")
        content = self.request.get("content")

        self.response.headers['Content-Type'] = 'application/json'
        destination = Destination.add(user=self.user, title=title, content=content)
        response = {
            "destination": {
                "_id": destination.key.id(),
                "title": destination.title,
                "content": destination.content,
                "createdDate": destination.created_date.isoformat(),
            }
        }
        self.response.out.write(json.dumps(response))


class DestinationGetAll(Handlers):
    @authenticate_user
    def get(self):
        destinations = Destination.get_all_by_specific_user(user=self.user)
        self.response.headers['Content-Type'] = 'application/json'

        list_of_json_destinations = []
        for destination in destinations:
            list_of_json_destinations.append({
                "_id": destination.key.id(),
                "title": destination.title,
                "content": destination.content,
                "createdDate": destination.created_date.isoformat(),
            })
        response = {
            "destinations": list_of_json_destinations,
        }
        self.response.out.write(json.dumps(response))


class DestinationGetSome(Handlers):
    @authenticate_user
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'


class DestinationUpdate(Handlers):
    @authenticate_user
    def post(self, user_key):
        destination_id = self.request.get("destination-id")
        title = self.request.get("title")
        content = self.request.get("content")
        destination_id = self.request.get("destination-id")
        destination_id = Destination.update(destination_id)
        if destination_id:
            response = {
                "status": "success",
                "message": "Delete destination successfully",
            }
            self.response.out.write(json.dumps(response))
        else:
            response = {
                "status": "fail",
                "message": "Failed to delete destination",
            }
            self.response.set_status(403, message="Forbidden")
            self.response.out.write(json.dumps(response))


class DestinationDelete(Handlers):
    @authenticate_user
    def post(self, user_key):
        destination_id = self.request.get("destination-id")
        destination_id = Destination.delete(destination_id)
        if destination_id:
            response = {
                "status": "success",
                "message": "Delete destination successfully",
            }
            self.response.out.write(json.dumps(response))
        else:
            response = {
                "status": "fail",
                "message": "Failed to delete destination",
            }
            self.response.set_status(403, message="Forbidden")
            self.response.out.write(json.dumps(response))
