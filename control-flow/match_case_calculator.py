# match_case_calculator.py  

# Prompt for User Input  
num1 = float(input("Enter the first number: "))  
num2 = float(input("Enter the second number: "))  
operation = input("Choose the operation (+, -, *, /): ")  

# Perform the Calculation Using Match Case  
match operation:  
    case '+':  
        result = num1 + num2  
    case '-':  
        result = num1 - num2  
    case '*':  
        result = num1 * num2  
    case '/':  
        if num2 == 0:  
            result = "Cannot divide by zero."  
        else:  
            result = num1 / num2  
    case _:  
        result = "Invalid operation."  

# Output the Result  
print(f"The result is {result}.")