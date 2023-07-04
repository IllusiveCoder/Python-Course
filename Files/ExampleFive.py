# If statement
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")

# For loop
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")

# While loop
count = 0

while count < 5:
    print("Count:", count)
    count += 1

# Nested control structures
for i in range(1, 4):
    print("Outer loop:", i)
    
    for j in range(1, 4):
        print("Inner loop:", j)

# Break and continue statements
for number in range(1, 6):
    if number == 3:
        break
    print(number)

for number in range(1, 6):
    if number == 3:
        continue
    print(number)
