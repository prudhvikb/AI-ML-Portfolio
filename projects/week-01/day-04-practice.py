#Calculate the area of a circle  given its radius.
import math
def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = math.pi * (radius ** 2)
    return area
print(calculate_circle_area(9))

count = 0
while count < 5:
    print("Count is:", count)
    count += 1

for i in range(1,11):
    print("order is:", i)

list_of_numbers = [1, 2, 3, 4, 5]
def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print("Sum of numbers:", sum_of_numbers(list_of_numbers))

def greet(Prudhvi):
    print(f"Hello, {Prudhvi}!")
greet("Prudhvi")

def larger_number(a,b):
    if a > b:
        return a
    else:
        return b
print(larger_number(10, 20))

book = { "title" : "The Alchemist", "author" : "Paulo Coelho", "year" : 1988, "genre": "Fiction" }
book["rating"] = 4.5
print(book)

def about_book(book):
    for key, value in book.items():
        print(f"{key}: {value}")
    return book
print(about_book(book))

def even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("Even numbers:", even_numbers(numbers))

def average(numbers):
    return sum(numbers)/len(numbers)

print("Average of numbers:", average(list_of_numbers))

students = [
    {"name": "Alice", "age": 16, "grade": "A"},
    {"name": "Bob", "age": 22, "grade": "B"},
    {"name": "Charlie", "age": 12, "grade": "C"}
]

def adult_students(students):
    return [student for student in students if student["age"] > 18]
print("Adult students:", adult_students(students))