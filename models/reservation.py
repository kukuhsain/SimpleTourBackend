from google.appengine.ext import ndb


class Reservation(ndb.Model):
    guest_id = ndb.IntegerProperty()
    package_id = ndb.IntegerProperty()
    price_per_person = ndb.FloatProperty()
    number_of_people = ndb.IntegerProperty()
    created_date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def add(cls, guest, package, price_per_person, number_of_people):
        reservation = cls(guest_id=guest.key.id(), package_id=guest.key.id())
        if price_per_person.isdigit():
            reservation.price_per_person = float(price_per_person)
        if number_of_people.isdigit():
            reservation.number_of_people = int(number_of_people)
        reservation.put()
        return reservation

    @classmethod
    def get_all(cls):
        reservations = cls.query().fetch()
        return reservations

    @classmethod
    def update(cls, reservation_id, guest, package, price_per_person, number_of_people):
        reservation = cls.get_by_id(int(reservation_id))
        if reservation:
            reservation.guest_id = guest.key.id()
            reservation.package_id = package.key.id()
            if price_per_person.isdigit():
                reservation.price_per_person = float(price_per_person)
            if number_of_people.isdigit():
                reservation.number_of_people = int(number_of_people)
            reservation.put()
            return reservation
        else:
            return False

    @classmethod
    def delete(cls, reservation_id):
        reservation = cls.get_by_id(int(reservation_id))
        if reservation:
            reservation.key.delete()
            return True
        else:
            return False
