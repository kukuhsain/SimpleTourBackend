from base_controller import Handlers
from models.package import Package
from models.reservation import Reservation


class ReservationAdd(Handlers):
    def post(self):
        guest = self._authenticate_user_guest()
        if guest:
            package_id = self.request.get("package_id")
            if package_id.isdigit():
                package = Package.get_by_id(int(package_id))
                if package:
                    price_per_person = self.request.get("price_per_person")
                    number_of_people = self.request.get("number_of_people")
                    reservation = Reservation.add(guest, package, price_per_person, number_of_people)
                    response = {
                        "reservationId": reservation.key.id(),
                        "pricePerPerson": reservation.price_per_person,
                        "numberOfPeople": reservation.number_of_people,
                        "createdDate": reservation.created_date.isoformat(),
                        "package": {
                            "packageId": package.key.id(),
                            "title": package.title,
                            "content": package.content,
                            "location": package.location,
                            "price": package.price,
                            "imageUrl": "/image?image_id=" + str(package.image_id),
                            "createdDate": package.created_date.isoformat(),
                        }
                    }
                    self._response_json(response)
                else:
                    self._raise_404_response()
            else:
                self._raise_404_response()


class ReservationGetAll(Handlers):
    def get(self):
        reservations = Reservation.get_all()
        list_of_json_reservations = []
        for reservation in reservations:
            print "reservation package id..."
            print reservation.package_id
            package = Package.get_by_id(int(reservation.package_id))
            print package
            list_of_json_reservations.append({
                "reservationId": reservation.key.id(),
                "pricePerPerson": reservation.price_per_person,
                "numberOfPeople": reservation.number_of_people,
                "createdDate": reservation.created_date.isoformat(),
                # "package": {
                #     "packageId": package.key.id(),
                #     "title": package.title,
                #     "content": package.content,
                #     "location": package.location,
                #     "price": package.price,
                #     "imageUrl": "/image?image_id=" + str(package.image_id),
                #     "createdDate": package.created_date.isoformat(),
                # }
            })
        response = list_of_json_reservations
        self._response_json(response)
