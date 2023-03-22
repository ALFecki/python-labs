from storage import Storage


def main():

    storage = Storage()
    
    while True:

        if not storage.isinitiaziled():
            username = input("Username: >>>> ")
            storage.set_user(username)
            load_desicion = input("You want to load data (y/n) >>>>")

            if load_desicion == "y" or load_desicion == "":
                storage.load()


        command = input(">>>> ")
        

        if "add" in command:
            storage.add(command)
            continue

        if "remove" in command:
            storage.remove(command)
            continue

        if "save" in command:
            storage.save()

        if "quit" in command:
            break   





if __name__ == "__main__":
    main()
