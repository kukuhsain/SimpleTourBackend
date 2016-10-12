import requests


class UserAuth:
    def __init__(self, base_url, email, password):
        self.base_url = base_url
        self.email = email
        self.password = password
        self.access_token = ""

    def _get_dict_data(self):
        return {
            "email": self.email,
            "password": self.password,
        }

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    def get_access_token(self):
        return self.access_token

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
        if r.status_code == 200:
            self.access_token = r.json()['access_token']
        else:
            self.access_token = ""

    def logout(self):
        url = self.base_url + "/user/logout"
        r = requests.post(url, data={"access_token": self.access_token})
        print r
        print r.text
