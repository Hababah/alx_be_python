# Global Conversion Factors  
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  

def convert_to_celsius(fahrenheit):  
    """Convert Fahrenheit to Celsius using the global conversion factor."""  
    global FAHRENHEIT_TO_CELSIUS_FACTOR  
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR  

def convert_to_fahrenheit(celsius):  
    """Convert Celsius to Fahrenheit using the global conversion factor."""  
    global CELSIUS_TO_FAHRENHEIT_FACTOR  
    return (celsius * 1 / CELSIUS_TO_FAHRENHEIT_FACTOR) + 32  

def main():  
    try:  
        # User Interaction  
        temperature_input = input("Enter the temperature to convert: ")  
        temperature = float(temperature_input)  
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()  
        
        if unit == 'F':  
            converted = convert_to_celsius(temperature)  
            print(f"{temperature}°F is {converted}°C")  
        elif unit == 'C':  
            converted = convert_to_fahrenheit(temperature)  
            print(f"{temperature}°C is {converted}°F")  
        else:  
            raise ValueError("Invalid temperature unit. Please enter 'C' or 'F'.")  
    except ValueError as e:  
        print(f"Invalid temperature. {e}")  
    except Exception as e:  
        print(f"An error occurred: {e}")  

if __name__ == "__main__":  
    main()