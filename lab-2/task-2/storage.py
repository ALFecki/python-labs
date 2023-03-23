import ujson
import os
import re


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

        if not os.path.exists("storage.json"):
            storage_file = open("storage.json", "w+")
        with open("storage.json", "r+") as storage_file:
            
            try:
                data_list = ujson.load(storage_file)
                user_in_json = next((item for item in data_list if item['user'] == self.user), None)
                if user_in_json:
                    self.container.update(set(user_in_json['container']))
                    data_list.remove(user_in_json)
                
            except:
                data_list = []

            data_list.append(self.serialize())
            storage_file.seek(0)
            ujson.dump(data_list, storage_file)



    def load(self):
        if not os.path.exists("storage.json"):
            open("storage.json", "w+")
            print("File storage.json cannot find. File created")
            return
        with open("storage.json") as storage_file:
            try:
                data_list = ujson.load(storage_file)
            except:
                return
            self.deserialize(
                next((st for st in data_list if st["user"] == self.user), None)
            )

    def find(self, data: str):
        if not self.isinitiaziled():
            print("User is not initialized")
            return
        
        data = data.removeprefix("find ")
        return next((item for item in self.container if item == data), None)
            

    def grep(self, regex: str):
        if not self.isinitiaziled():
            print("User is not initialized")
            return
        
        regex = fr'{regex.removeprefix("grep ")}'
        founded_list = []
        for item in self.container:
            if re.match(regex, item):
                founded_list.append(item)

        return founded_list
        
    def list_elements(self):
        return self.container


    def switch(self, username: str):
        self.user = username.removeprefix("switch ")
        self.container = set()


    def serialize(self):
        return dict({"user": self.user, "container": list(self.container)})

    def deserialize(self, input: dict):
        if input == None:
            print("No such user")
            return
        self.user = input["user"]
        self.container = set(input["container"])
