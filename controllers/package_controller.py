from base_controller import Handlers
from models.destination import Destination
from models.package import Package


class PackageAdd(Handlers):
    def post(self, destination_id):
        host = self._authenticate_user_host()
        if host:
            if destination_id.isdigit():
                destination = Destination.get_by_id(int(destination_id))
                if destination:
                    title = self.request.get("title")
                    content = self.request.get("content")
                    location = self.request.get("location")
                    image = self.request.get("image")
                    price = self.request.get("price")

                    package = Package.add(int(destination_id), title, content, location, image, price)
                    response = {
                        "packageId": package.key.id(),
                        "title": package.title,
                        "content": package.content,
                        "location": package.location,
                        "price": package.price,
                        "imageUrl": "/image?image_id=" + str(package.image_id),
                        "createdDate": package.created_date.isoformat(),
                    }
                    self._response_json(response)
                else:
                    self._raise_404_response()
            else:
                self._raise_404_response()


class PackageGetAll(Handlers):
    def get(self, destination_id):
        if destination_id.isdigit():
            destination = Destination.get_by_id(int(destination_id))
            if destination:
                packages = Package.get_all_by_destination_id(int(destination_id))
                list_of_json_packages = []
                for package in packages:
                    list_of_json_packages.append({
                        "packageId": package.key.id(),
                        "title": package.title,
                        "content": package.content,
                        "location": package.location,
                        "price": package.price,
                        "imageUrl": "/image?image_id=" + str(package.image_id),
                        "createdDate": package.created_date.isoformat(),
                    })
                response = list_of_json_packages
                self._response_json(response)
            else:
                self._raise_404_response()
        else:
            self._raise_404_response()


class PackageGetOne(Handlers):
    def get(self, destination_id, package_id):
        if destination_id.isdigit():
            destination = Destination.get_by_id(int(destination_id))
            if destination:
                if package_id.isdigit():
                    package = Package.get_by_id(int(package_id))
                    if package:
                        response = {
                            "packageId": package.key.id(),
                            "title": package.title,
                            "content": package.content,
                            "location": package.location,
                            "price": package.price,
                            "imageUrl": "/image?image_id=" + str(package.image_id),
                            "createdDate": package.created_date.isoformat(),
                        }
                        self._response_json(response)
                    else:
                        self._raise_404_response()
                else:
                    self._raise_404_response()
            else:
                self._raise_404_response()
        else:
            self._raise_404_response()


class PackageUpdate(Handlers):
    def post(self, destination_id):
        host = self._authenticate_user_host()
        if host:
            if destination_id.isdigit():
                destination = Destination.get_by_id(int(destination_id))
                if destination:
                    package_id = self.request.get("package_id")
                    title = self.request.get("title")
                    content = self.request.get("content")
                    location = self.request.get("location")
                    price = self.request.get("price")

                    if package_id.isdigit():
                        package = Package.update(int(destination_id), int(package_id), title, content, location, price)
                        if package:
                            response = {
                                "packageId": package.key.id(),
                                "title": package.title,
                                "content": package.content,
                                "location": package.location,
                                "price": package.price,
                                "imageUrl": "/image?image_id=" + str(package.image_id),
                                "createdDate": package.created_date.isoformat(),
                            }
                            self._response_json(response)
                        else:
                            self._raise_500_response()
                    else:
                        self._raise_404_response()
                else:
                    self._raise_404_response()
            else:
                self._raise_404_response()


class PackageDelete(Handlers):
    def post(self, destination_id):
        host = self._authenticate_user_host()
        if host:
            if destination_id.isdigit():
                destination = Destination.get_by_id(int(destination_id))
                if destination:
                    package_id = self.request.get("package_id")
                    if package_id.isdigit():
                        result = Package.delete(int(package_id))
                        if result:
                            response = {
                                "status": "success",
                                "message": "Delete package successfully",
                            }
                            self._response_json(response)
                        else:
                            self._raise_500_response()
                    else:
                        self._raise_404_response()
                else:
                    self._raise_404_response()
            else:
                self._raise_404_response()
