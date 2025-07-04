#variables
name = "Prudhvi"
age = 25
is_learning = True

print(f"Name: {name}, Age: {age}, Learning: {is_learning}")

# Simple arithmetic
a = 2
b = 10
print("Addition:", a + b)
print("Division:", a / b)
print("Multiplication:", a * b)
print("Subtraction:", a - b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# Importing datetime module to display current date and time
from datetime import datetime
print(f"Today's date is: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Define a function
def greet(user):
    return f"Hello {user}, keep up the great work!"

print(greet(name))