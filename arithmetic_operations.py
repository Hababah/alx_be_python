# Arithmetic_Operations.py

def perform_operation(num1, num2, operation):

    match operation:
        case "add":
            return  num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num1 != 0:
                return num1 / num2
            else:
                print("Invalid input, num1 must be greater than zero ")
        case _:
            print("Unrecognised input, input add/subtract/multiply/divide ")

    



