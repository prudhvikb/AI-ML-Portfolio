# Data Types

text = "Day 2 start" #string
count = 7 #int
pi = 3.14 #float
learning = True #boolean
topics = ["python", "AI", "ML"] #list
info = {"name":"prudhvi", "task":"learn"} #dic
none_value = None #none

print(type(text), type(count), type(pi), type(learning), 
      type(topics), type(info), type(none_value))

# Conditional Statements

score = 85

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

# --- LISTS & LOOPS ---
skills = ["Variables", "Data Types", "Conditionals", "Loops"]

print("\n" + "Skills practiced so far:")
for i, skill in enumerate(skills, start=1):
    print(f"{i}. {skill}")

count = 0
while count < 3:
    print("Learning is fun!")
    count += 1

for i in range(5):
    print("Step", i)



# --- FUNCTIONS ---
def describe_person(name, age, learning=True):
    status = "is learning" if learning else "not learning"
    return f"{name} is {age} years old and is {status}."

print("\n" + describe_person("Prudhvi", 25))
print(describe_person("Alex", 30, learning=False))