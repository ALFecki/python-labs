
import os

def arithmetic_operation(first, second, operation):
    match operation:
        case os.environ.get('ADD'):
            return first + second
        case os.environ.get('SUB'):
            return first - second
        case os.environ.get('MUL'):
            return first * second
        case os.environ.get('DIV'):
            return first / second
        case _:
            print("Invalid operation!")


