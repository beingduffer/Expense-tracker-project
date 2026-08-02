from database import create_table, add_expense, total_expense, expense_by_category, show_table

def menu():
    create_table()
    username = input("Enter your username: ")

    while True:
        print(f"\n--- Expense Tracker ({username}) ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Expenses")
        print("4. Spend by Category")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(username)
        elif choice == "2":
            show_table(username)
        elif choice == "3":
            total_expense(username)
        elif choice == "4":
            expense_by_category(username)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    menu()