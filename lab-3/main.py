import sys

sys.path.append("..")


from serialization_tool.extension.extension import Extension

def add(a, b):
    return a + b

def main():
    
    json = Extension.get_file_extension("json")
    c = {2: 'a', 3: 'b'}
    a = 4
    b = 2.5
    
    # json.dump([a, b, c], "example.json")
    json.dump(add, "example.json")
    print(json.load("example.json"))



if __name__ == "__main__":
    main()