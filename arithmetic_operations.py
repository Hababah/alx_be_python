from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    def perform_operation(num1, num2, operation):
        
        match operation:
            case "add":
                num1 + num2
            case "subtract":
                num1 - num2
            case "multiply":
                num1 * num2
            case "divide":
                if num1 != 0:
                    num1 / num2
                else:
                    print("Invalid input, num1 must be greater than zero ")
            case _:
                print("Unrecognised input, input add/subtract/multiply/divide ")

    
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()



