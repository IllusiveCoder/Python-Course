# Data Handling: File Operations
try:
    # Opening a file in read mode
    file = open("data.txt", "r")
    
    # Reading and printing the contents of the file
    data = file.read()
    print("File Contents:", data)
    
    # Closing the file
    file.close()

except FileNotFoundError:
    print("File not found.")
    
except PermissionError:
    print("Permission denied while accessing the file.")

# Data Handling: Data Manipulation
numbers = [5, 2, 7, 1, 9]

# Sorting the list in ascending order
sorted_numbers = sorted(numbers)
print("Sorted Numbers:", sorted_numbers)

# Finding the maximum value in the list
max_value = max(numbers)
print("Maximum Value:", max_value)

# Exception Handling: ZeroDivisionError
try:
    numerator = 10
    denominator = 0
    
    # Performing division
    result = numerator / denominator
    
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

# Exception Handling: ValueError
try:
    age = int(input("Enter your age: "))
    print("Your age:", age)

except ValueError:
    print("Invalid input. Please enter a valid integer.")

# Exception Handling: Custom Exception
class CustomException(Exception):
    pass

try:
    # Raising a custom exception
    raise CustomException("This is a custom exception.")

except CustomException as e:
    print("Custom Exception:", str(e))