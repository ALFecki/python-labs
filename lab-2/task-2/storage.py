import ujson
import json
import os


class Storage:
    user: str
    container: set

    def __init__(self, username: str = None, container: set = set()):
        self.user = username
        self.container = container

    def isinitiaziled(self):
        return self.user != None

    def set_user(self, user: str):
        self.user = user

    def add(self, data: str):
        if not self.isinitiaziled():
            print("User is not initialized")
            return

        data = data.removeprefix("add ")
        if len(data) > 0:
            if next((item for item in self.container if item == data), None):
                print("These element already exists")
                return
            self.container.add(data)
        else:
            print("Invalid input")

    def remove(self, data: str):
        if not self.isinitiaziled():
            print("User is not initialized")
            return

        try:
            data = data.split(" ")[1]
            if len(data) > 0:
                self.container.remove(data)
        except:
            print("Invalid input")
            return

    def save(self):
        if not self.isinitiaziled():
            print("User is not initialized")
            return

        if not os.path.exists(".\storage.json"):
            storage_file = open("storage.json", "w+")
        storage_file = open("storage.json", "r+")
        data_list = ujson.load(storage_file)
        if next((item for item in data_list if item['user'] == self.user), None):
            print("User already exists")
            return
        data_list.append(self.serialize())
        storage_file.seek(0)
        ujson.dump(data_list, storage_file)

    def load(self):
        with open("storage.json") as storage_file:
            data_list = ujson.load(storage_file)

            self.deserialize(
                next((st for st in data_list if st["user"] == self.user), None)
            )

    def serialize(self):
        return dict({"user": self.user, "container": list(self.container)})

    def deserialize(self, input: dict):
        self.user = input["user"]
        self.container = set(input["container"])
