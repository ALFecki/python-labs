
from utilities import arithmetic_operation

def main():
    print("Hello, World!")
    
    first = int(input("Please enter first number: "))

    second = int(input("Please enter second number: "))

    operation = str(input("Please enter operation: "))
    
    res = arithmetic_operation(first, second, operation)
    print("Result is ", res)

    

    





if __name__ == "__main__":
    main()