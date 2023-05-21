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

        if "load" in command:
            storage.load()

        if "find" in command:
            founded = storage.find(command)
            if founded:
                print("Founded is ", founded)
            else:
                print("No such elements")

        if "grep" in command:
            founded = storage.grep(command)
            if founded:
                print("Founded is ", founded)
            else:
                print("No such elements")

        if "list" in command:
            print("List of elements: ", storage.list_elements())

        if "switch" in command:
            save_desicion = input("You want to save data (y/n) >>>>")
            if save_desicion == "y" or save_desicion == "":
                storage.save()
                
            storage.switch(command)

            load_desicion = input("You want to load data (y/n) >>>>")
            if load_desicion == "y" or load_desicion == "":
                storage.load()

        if "quit" in command:
            save_desicion = input("You want to save data (y/n) >>>>")
            if save_desicion == "y" or save_desicion == "":
                storage.save()
            break   





if __name__ == "__main__":
    main()
