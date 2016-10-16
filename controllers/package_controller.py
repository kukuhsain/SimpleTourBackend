from base_controller import Handlers
from models.package import Package


class PackageAdd(Handlers):
    def post(self):
        admin = self._authenticate_admin()
        if admin:
            title = self.request.get("title")
            content = self.request.get("content")
            location = self.request.get("location")
            image = self.request.get("image")
            price = self.request.get("price")

            package = Package.add(title, content, location, image, price)
            response = {
                "package_id": package.key.id(),
                "title": package.title,
                "content": package.content,
                "location": package.location,
                "price": package.price,
                "image_url": "/image?image_id=" + str(package.image_id),
                "created_date": package.created_date.isoformat(),
            }
            self._response_json(response)


class PackageGetAll(Handlers):
    def get(self):
        packages = Package.get_all()
        list_of_json_packages = []
        for package in packages:
            list_of_json_packages.append({
                "package_id": package.key.id(),
                "title": package.title,
                "content": package.content,
                "location": package.location,
                "price": package.price,
                "image_url": "/image?image_id=" + str(package.image_id),
                "created_date": package.created_date.isoformat(),
            })
        response = list_of_json_packages
        self._response_json(response)


class PackageGetOne(Handlers):
    def get(self, package_id):
        if package_id.isdigit():
            package = Package.get_by_id(int(package_id))
            if package:
                response = {
                    "package_id": package.key.id(),
                    "title": package.title,
                    "content": package.content,
                    "location": package.location,
                    "price": package.price,
                    "image_url": "/image?image_id=" + str(package.image_id),
                    "created_date": package.created_date.isoformat(),
                }
                self._response_json(response)
            else:
                self._raise_404_response()
        else:
            self._raise_404_response()


class PackageUpdate(Handlers):
    def post(self, user_key):
        admin = self._authenticate_admin()
        if admin:
            package_id = self.request.get("package_id")
            title = self.request.get("title")
            content = self.request.get("content")
            location = self.request.get("location")
            price = self.request.get("price")

            package = Package.update(package_id, title, content, location)
            if package:
                response = {
                    "package_id": package.key.id(),
                    "title": package.title,
                    "content": package.content,
                    "location": package.location,
                    "price": package.price,
                    "image_url": "/image?image_id=" + str(package.image_id),
                    "created_date": package.created_date.isoformat(),
                }
                self._response_json(response)
            else:
                self._raise_500_response()

class PackageDelete(Handlers):
    def post(self, user_key):
        admin = self._authenticate_admin()
        if admin:
            package_id = self.request.get("package_id")
            result = Package.delete(package_id)
            if result:
                response = {
                    "status": "success",
                    "message": "Delete package successfully",
                }
                self._response_json(response)
            else:
                self._raise_500_response()
