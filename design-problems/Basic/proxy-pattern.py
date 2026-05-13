class User():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class RealUser(User):
    def __init__(self, name):
        super().__init__(name)
        # Simulate a costly operation, e.g., fetching user data from a database
        print(f"Loading user data for {name}...")


class ProxyUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.real_user = None

    def get_name(self):
        if self.real_user is None:
            self.real_user = RealUser(self.name)  # Lazy initialization
        return self.real_user.get_name()


proxy_user = ProxyUser("Alice")
print("Proxy user created. Real user data not loaded yet.")
print(f"User name: {proxy_user.get_name()}")  # Real user data will
print(f"User name again: {proxy_user.get_name()}")  # Real user data already loaded, no delay