# User input
name = input("Enter your name: ")  # Prompt the user to enter their name
age = int(input("Enter your age: "))  # Prompt the user to enter their age

# Output to the console
print("Name:", name)  # Print the entered name
print("Age:", age)  # Print the entered age

# File I/O - Reading from a file
with open("data.txt", "r") as file:  # Open the file for reading
    content = file.read()  # Read the entire contents of the file
    print("File Contents:")
    print(content)  # Print the contents of the file

# File I/O - Writing to a file
output_content = "This is some content that will be written to the file."
with open("output.txt", "w") as file:  # Open the file for writing
    file.write(output_content)  # Write the content to the file

print("Output file 'output.txt' has been written with the provided content.")

# Error handling
try:
    # Trying to read from a non-existent file
    with open("nonexistent.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'nonexistent.txt' does not exist.")
