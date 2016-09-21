from generators import *

base_url = "http://localhost:8080"
email = "test@email.com"
password = "111111"

user = UserAuth(base_url, email, password)
user.register()
user.login()

user.set_password("222222")
user.login()
