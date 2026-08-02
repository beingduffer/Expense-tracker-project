import matplotlib.pyplot as plt
from database import expense_by_category

def show_spending_chart(username):
    data = expense_by_category(username)

    if not data:
        print("No expenses to show yet.")
        return

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title(f"Spending by Category - {username}")
    plt.show()