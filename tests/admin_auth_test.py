import unittest
import requests


class TestAdminAuth(unittest.TestCase):
    def __init__(self, *args):
        super(TestAdminAuth, self).__init__(*args)
        self.base_url = "http://localhost:8080"
        self.admin_data = {
            "email": "admin@test.com",
            "password": "test",
        }
        self.access_token = ""

    def test_1_register(self):
        url = self.base_url + "/admin/register"
        r = requests.post(url, data=self.admin_data)
        result = self.assertEqual(r.status_code, 200)
        if not result:
            r2 = requests.post(url, data=self.admin_data)
            self.assertEqual(r2.status_code, 500)

    def test_2_login(self):
        url = self.base_url + "/admin/login"
        r = requests.post(url, data=self.admin_data)
        self.assertEqual(r.status_code, 200)
        self.access_token = r.json()['access_token']
        print "access token..."
        print self.access_token

    def test_3_logout(self):
        url = self.base_url + "/admin/logout"

        r = requests.post(url, data={"access_token": self.access_token})
        self.assertEqual(r.status_code, 200)


if __name__ == "__main__":
    unittest.main()