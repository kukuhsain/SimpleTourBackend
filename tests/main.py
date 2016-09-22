import time
from generators import *

# Initialization
base_url = "http://localhost:8080"
email = "test@email.com"
password = "111111"

# Setup user auth
user = UserAuth(base_url, email, password)
user.register()
time.sleep(0.5)

# Test for login and logout
user.login()
user.logout()

# Test for incorrect password and closed session
user.set_password("222222")
user.login()
user.logout()

# Get user's access token
user.set_password("111111")
user.login()
access_token = user.get_access_token()

# Initiate dummy data
title = "The Title of Lorem Ipsum"
content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec erat lacus, scelerisque sit amet tempus in, aliquam ac tortor. Nunc ultricies orci sed lacus semper sollicitudin. Donec pharetra erat mauris, a vehicula est consectetur in. Aliquam consequat tristique purus et aliquet. Donec malesuada, turpis nec sollicitudin auctor, ipsum nisl tincidunt libero, sed ornare quam urna sed mauris. Phasellus vel convallis mauris. Vestibulum at diam sit amet dolor eleifend porttitor. Phasellus vitae accumsan elit. Mauris pellentesque fringilla rutrum. Nam eget euismod lectus. Integer varius enim sed magna porttitor rhoncus sit amet nec nunc.

Duis consectetur urna vitae elit dapibus mattis. Phasellus vel sem hendrerit enim molestie pulvinar. Nullam suscipit lacus purus, eu luctus mi iaculis sed. Vivamus eu est sapien. Praesent vehicula augue id cursus iaculis. Proin eu erat mauris. Aliquam eu felis ullamcorper, sodales eros at, blandit ante. Quisque bibendum euismod metus. Integer sit amet nibh non elit mattis semper. Nunc tincidunt tortor sit amet ultricies dignissim. Maecenas ipsum nunc, sagittis vel facilisis quis, gravida ac diam. Phasellus a maximus diam, vitae volutpat nisi."""

# Test for note
note = NoteGenerator(base_url, access_token, title, content)
note.add()
