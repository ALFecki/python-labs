import sys

sys.path.append("..")


from serialization_tool.extension.extension import Extension

def main():
    
    json = Extension.get_file_extension("json")
    b = {2: 'a', 3: 'b'}
    a = 4
    json.dump(a, "example.json")
    print(json.loads("example.json"))



if __name__ == "__main__":
    main()