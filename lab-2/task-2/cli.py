from storage import Storage
import ujson

class InteractiveCLI:
    storages: list


    def __init__(self) -> None:
        pass


    def save(self):
        pass


    def load(self):
        storage_file = open("storage.json")
        self.storages = ujson.load(storage_file)['storages']
        # data_list.index(self)