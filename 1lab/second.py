import configparser
from configparser import ConfigParser


class User:
    def __init__(self, login, password, name, surname):
        self.login = login
        self.password = password
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Login = {self.login}, password = {self.password}, name = {self.name}, surname = {self.surname}"


config = ConfigParser()
config.read("second.ini")
user1 = User("Login1", "Password1", "Name1", "Surname1")
try:
    config.add_section("section_user2")
    config.set("section_user2", "login", "login2")
    config.set("section_user2", "password", "password2")
    config.set("section_user2", "name", "name2")
    config.set("section_user2", "surname", "surname2")
    print("User2 was added to file")
except configparser.DuplicateSectionError:
    print("User2 already in file")

user2 = User(
    # config.get("section_user2", "login"),
    # config.get("section_user2", "password"),
    # config.get("section_user2", "name"),
    # config.get("section_user2", "surname")
    config["section_user2"]["login"],
    config["section_user2"]["password"],
    config["section_user2"]["name"],
    config["section_user2"]["surname"]
)
print(user2)
users = [user1, user2]
i = 0
for user in users:
    i += 1
    try:
        config.add_section(f"section_user{i}")
        config.set(f"section_user{i}", "login", str(user.login))
        config.set(f"section_user{i}", "password", str(user.password))
        config.set(f"section_user{i}", "name", str(user.name))
        config.set(f"section_user{i}", "surname", str(user.surname))
        print(f"User{i} was added to file")
    except configparser.DuplicateSectionError:
        print("User2 already in file")
with open("second.ini", "w") as f:
    config.write(f)

print(config.keys())

