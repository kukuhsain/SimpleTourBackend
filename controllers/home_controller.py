from base_controller import Handlers


class Home(Handlers):
    def get(self):
        self.response.write("Hello, welcome to SimpleNote")
