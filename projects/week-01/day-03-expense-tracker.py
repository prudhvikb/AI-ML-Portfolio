def collect_expenses(item_name):
    expenses = []
    while True:
        entry = input(f"Enter the expense for {item_name} (or 'done' to finish): ")
        if entry.lower() == 'done':
            break
        try:
            expenses.append(float(entry))
        except ValueError:
            print("Invalid input. Please enter a valid number or 'done'.")
    return expenses

pens_expenses = collect_expenses("pens")
pencils_expenses = collect_expenses("pencils")
erasers_expenses = collect_expenses("erasers")
notebooks_expenses = collect_expenses("notebooks")

categories = [
    ("pens", pens_expenses),
    ("pencils", pencils_expenses),
    ("erasers", erasers_expenses),
    ("notebooks", notebooks_expenses)
]

for name, category_expenses in categories:
    print(f"{name.capitalize()} expenses: {category_expenses}")
    if category_expenses:
        avg = sum(category_expenses) / len(category_expenses)
        print(f"Average {name} expense: {avg:.2f}")
    else:
        print(f"No expenses entered for {name}.")

total_expense = sum(sum(expenses) for _, expenses in categories)
print(f"Total expense: {total_expense}")
average_expense = total_expense / len(categories)
print(f"Average expense across all categories: {average_expense}")

with open("expenses_report.txt", "w") as f:
    f.write("Expense Report\n")
    f.write("====================\n")
    for name, expenses in categories:
        f.write(f"{name.capitalize()} expenses: {expenses}\n")
        if expenses:
            avg = sum(expenses) / len(expenses)
            f.write(f"Average {name} expense: {avg:.2f}\n")
            f.write(f"Sum {name} expense: {sum(expenses):.2f}\n")
        else:
            f.write(f"No expenses entered for {name}.\n")
        f.write("\n")
    f.write(f"Total expense: {total_expense:.2f}\n")
    f.write(f"Average expense across all categories: {average_expense:.2f}\n")

print("Expenses written to expenses_report.txt")