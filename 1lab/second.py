import configparser
import argparse
from configparser import ConfigParser
from Classes import User
import os

parser = argparse.ArgumentParser(description="Argument parser for path argument")
parser.add_argument('-p', '--path', default='Settings\\second.ini', help="Path to ini file")
args = parser.parse_args()

config = ConfigParser()
config.read(args.path)

if not os.path.exists("Settings"):
    os.mkdir("\\Settings")
    print(f"Folder {os.getcwd()}\\Settings has been created")

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

with open(args.path, "w") as f:
    config.write(f)

config2 = ConfigParser()
config2.read(args.path)

user2 = User(
    # config2.get("section_user2", "login"),
    # config2.get("section_user2", "password"),
    # config2.get("section_user2", "name"),
    # config2.get("section_user2", "surname")
    config2["section_user2"]["login"],
    config2["section_user2"]["password"],
    config2["section_user2"]["name"],
    config2["section_user2"]["surname"]
)
# print(user2)
users = [user1, user2]
i = 0
for user in users:
    i += 1
    try:
        config2.add_section(f"section_user{i}")
        config2.set(f"section_user{i}", "login", str(user.login))
        config2.set(f"section_user{i}", "password", str(user.password))
        config2.set(f"section_user{i}", "name", str(user.name))
        config2.set(f"section_user{i}", "surname", str(user.surname))
        print(f"User{i} was added to file")
    except configparser.DuplicateSectionError:
        print(f"User{i} already in file")

with open(args.path, "w") as f:
    config2.write(f)

