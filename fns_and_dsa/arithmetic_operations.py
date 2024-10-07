# Arithmetic_Operations.py

def perform_operation(num1, num2, operation):  # Peforming the operations

    if operation == "add":
        return  num1 + num2
    elif operation =="subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return num1 / num2
        else:
            print("Invalid input, num1 must be greater than zero ")
    else:
        print("Unrecognised input, input add/subtract/multiply/divide ")

    



