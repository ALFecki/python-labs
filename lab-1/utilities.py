

OPERATION_DICT = {'+': ["add", "+", "addition"], '-':["sub", "-", "subtraction"], '*': ["mul", "*", "multiplication"], '/':["div", "/", "division"]}


def arithmetic_operation(first, second, operation):
    
    for (key, oper) in OPERATION_DICT.items():
        if oper.__contains__(operation):
            operation = key
            break
    
    match operation:
        case "+":
            return first + second
        case "-":
            return first - second
        case "*":
            return first * second
        case "/":
            return first / second
        case _:
            print("Invalid operation!")


