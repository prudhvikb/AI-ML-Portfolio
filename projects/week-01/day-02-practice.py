#Even or Odd Number Check
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an even number."
    else:
        return f"{number} is an odd number."    
    
if __name__ == "__main__":
    num = int(input("Enter a number to check if it's even or odd: "))
    result = check_even_odd(num)
    print(result)       

# Grade Calculation based on score input
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# List of groceries with enumeration
Groceries = ["Apples", "Bananas", "Carrots", "Doughnuts"]

print("\nShopping List:")
for i , item in enumerate(Groceries, start=1):
    print(f"{i}.{item}")

name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

print(f"Hello {name}, you are {age} years old.")

if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

greet = int(input("How many time I shoulkd greet you? "))
for i in range(greet):
    print(f"Hello {name}!")
    
range = [1,2,3,4,5]

for i in range:
    print(i*i)

