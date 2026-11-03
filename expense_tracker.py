import csv

def add_expense():
    name = input("Expense name: ")
    amount = float(input("Amount: "))
    category = input("Category: ")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, amount, category])

    print("Expense saved!")

def view_expenses():
    total = 0
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"{row[0]} | Rs.{row[1]} | {row[2]}")
                total += float(row[1])
        print(f"Total spent: Rs.{total}")
    except FileNotFoundError:
        print("No expenses yet.")

while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice, try again.")