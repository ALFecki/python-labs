
def arithmetic_operation(first, second, operation):
    match operation:
        case "add":
            return first + second
        case "sub":
            return first - second
        case "mul":
            return first * second
        case "div":
            return first / second
        case _:
            print("Invalid operation!")


