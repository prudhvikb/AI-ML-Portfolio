def add_item(item_list, item):
    item_list.append(item)
    return item_list

item_list = ["pen", "pencil", "eraser"]

add_item(item_list, "notebook")
print(item_list)

def remove_item(item_list, item):
    if item in item_list:
        item_list.remove(item)
    return item_list    

remove_item(item_list, "pencil")
print(item_list)


def is_positive(n):
    return n > 0
print(is_positive(5))  
print(is_positive(-3))  
print(is_positive(0))  

def print_all(items):
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item}")

items = ["apple", "banana", "cherry"]
print_all(items)

def get_number():
    num = input("Enter a number: ")
    if num.isdigit():
        print(f"sqaure of input number is {int(num) ** 2}")
        return None
    else:
        print("Invalid input. Please enter a valid number.")
    return get_number()

get_number()
