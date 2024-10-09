# from datetime import datetime, timedelta

# def display_current_datetime():
#     current_date = datetime.now
#     formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
#     print("Current Date and Time:", formatted_date)

from datetime import datetime, timedelta  

def display_current_datetime():  
    # Obtain the current date and time  
    current_date = datetime.now()  
    
    # Format the date and time in a readable format  
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  
    print(f"Current date and time: {formatted_date}")  

def calculate_future_date():  
    # Prompt the user for the number of days  
    try:  
        number_of_days = int(input("Enter the number of days to add to the current date: "))  
        # Calculate the future date  
        future_date = datetime.now() + timedelta(days=number_of_days)  
        
        # Format the future date  
        formatted_future_date = future_date.strftime("%Y-%m-%d")  
        print(f"Future date: {formatted_future_date}")  
    except ValueError:  
        print("Please enter a valid integer for the number of days.")  

if __name__ == "__main__":  
    display_current_datetime()  
    calculate_future_date()