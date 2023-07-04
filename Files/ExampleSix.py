# Lists
fruits = ['apple', 'banana', 'cherry', 'date']

# Accessing elements in a list
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Modifying elements in a list
fruits[1] = 'grape'
print("Modified fruits:", fruits)

# Tuples
coordinates = (10, 20, 30)

# Accessing elements in a tuple
print("First coordinate:", coordinates[0])
print("Last coordinate:", coordinates[-1])

# Sets
numbers = {1, 2, 3, 4, 5, 3, 2}

# Looping through a set
print("Numbers:")
for number in numbers:
    print(number)

# Dictionaries
student = {
    'name': 'John',
    'age': 20,
    'major': 'Computer Science'
}

# Accessing values in a dictionary
print("Student's name:", student['name'])
print("Student's age:", student['age'])
print("Student's major:", student['major'])

# Arrays (using NumPy)
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4, 5])

# Accessing elements in an array
print("First element:", array[0])
print("Last element:", array[-1])

# Linked List (using the llist module)
from llist import sllist

# Creating a linked list
linked_list = sllist([10, 20, 30, 40, 50])

# Accessing elements in a linked list
print("First node:", linked_list.first)
print("Last node:", linked_list.last)
