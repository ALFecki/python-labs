
from utilities import arithmetic_operation

def main():
    print("Hello, World!")
    
    print("Please enter first number: ")
    first = int(input)

    print("Please enter second number: ")
    second = int(input)

    print("Please enter operation: ")
    operation = str(input)
    
    res = arithmetic_operation(first, second, operation)
    print("Result is ", res)

    

    





if __name__ == "__main__":
    main()