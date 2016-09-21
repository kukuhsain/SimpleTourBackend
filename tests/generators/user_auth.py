import requests

class UserAuth():
    def __init__(self, base_url, email, password):
        self.base_url = base_url
        self.email = email
        self.password = password

    def _get_dict_data(self):
        return {
            "email": self.email,
            "password": self.password,
        }

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def register(self):
        url = self.base_url + "/user/register"
        print self._get_dict_data()
        r = requests.post(url, data=self._get_dict_data())
        print r
        print r.text

    def login(self):
        url = self.base_url + "/user/login"
        print self._get_dict_data()
        r = requests.post(url, data=self._get_dict_data())
        print r
        print r.text

    def logout(self):
        url = self.base_url + "/user/logout"
        print r
        print r.text
