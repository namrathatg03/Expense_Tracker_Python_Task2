import csv

# Function to add expense
def add_expense():
    desc = input("Enter description: ")
    amount = input("Enter amount: ")

    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])

    print("✅ Expense added successfully!\n")


# Function to view expenses
def view_expenses():
    try:
        with open("expenses.csv", "r") as f:
            print("\n📋 All Expenses:")
            for row in csv.reader(f):
                print(f"Item: {row[0]}, Amount: ₹{row[1]}")
    except FileNotFoundError:
        print("No expenses found.\n")


# Function to calculate total
def total_expenses():
    total = 0
    try:
        with open("expenses.csv", "r") as f:
            for row in csv.reader(f):
                total += int(row[1])
        print(f"\n💰 Total Expenses: ₹{total}\n")
    except FileNotFoundError:
        print("No expenses to calculate.\n")


# Main menu
def main():
    while True:
        print("==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice, try again.\n")


# Run program
main()