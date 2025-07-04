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