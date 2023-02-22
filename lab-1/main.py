
from utilities import arithmetic_operation

def main():
    print("Hello, World!")
    
    while True:
    
        first = int(input("Please enter first number: "))

        second = int(input("Please enter second number: "))

        operation = str(input("Please enter operation: "))
    
        res = arithmetic_operation(first, second, operation)
        print("Result is ", res)

        if str(input("Continue? (y/n)")) == "n":
            break

    list_of_numbers = []
    try:
        while True:
            list_of_numbers.append(int(input("Enter list number (enter non-integer to stop): ")))
    except:
        print("Your list is ", list_of_numbers)
        print("Even numbers of list are ", list(filter(lambda number: number % 2 == 0, list_of_numbers)))


if __name__ == "__main__":
    main()