import requests


class DestinationGenerator:
    def __init__(self, base_url, access_token, title, content):
        self.base_url = base_url
        self.access_token = access_token
        self.title = title
        self.content = content


    def _get_dict_access_token(self):
        return {
            "access_token": self.access_token
        }

    def _get_dict_data(self):
        return {
            "access_token": self.access_token,
            "title": self.title,
            "content": self.content,
        }

    def set_title(self, title):
        self.title = title

    def set_content(self, content):
        self.content = content

    def get_access_token(self):
        return self.access_token

    def add(self):
        url = self.base_url + "/note/add"
        print self._get_dict_data()
        r = requests.post(url, data=self._get_dict_data())
        print r
        print r.text

    def get_all(self):
        url = self.base_url + "/note/getall"
        r = requests.get(url, params=self._get_dict_access_token())
        print r
        print r.text

    def get_some(self):
        url = self.base_url + "/note/getsome"
        r = requests.get(url, data=self._get_dict_data())
        print r
        print r.text

    def delete(self):
        url = self.base_url + "/note/delete"
        r = requests.post(url, data={"access_token": self.access_token})
        print r
        print r.text
