# Function to add two numbers
def add_numbers():
    # Get the first number from the user and convert it to a float
    num1 = float(input("Enter the first number: "))
    
    # Get the second number from the user and convert it to a float
    num2 = float(input("Enter the second number: "))
    
    # Calculate the sum of the two numbers
    sum = num1 + num2
    
    # Print the result
    print(f"The sum of {num1} and {num2} is {sum}")

# Call the function
add_numbers()