

class User:
    def __init__(self, login, password, name, surname):
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Login = {self.login}, password = {self.password}, name = {self.name}, surname = {self.surname}"

