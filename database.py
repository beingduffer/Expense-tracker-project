import sqlite3

def create_connection():
    """Connects to (or creates) the expenses.db file."""
    conn = sqlite3.connect("expenses.db")
    return conn

def create_table():
    """Creates the expenses table if it doesn't already exist."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            Sno INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            date TEXT NOT NULL,
            category TEXT NOT NULL,
            description TEXT,
            amount REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_expense(username):
    conn = create_connection()
    cursor = conn.cursor()
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (e.g. Food, Travel, Rent): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))

    cursor.execute("""
        INSERT INTO expenses (Username,date, category, description, amount)
        VALUES (?, ?, ?, ?, ?)
    """, (username,date, category, description, amount))

    conn.commit()
    conn.close()
    print("Expense added successfully.")  

def total_expense(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses where Username=?",(username,))
    total = cursor.fetchone()
    conn.close()
    if total[0] is None :
        print("Total expense : 0")
    else:    
        print(f"Total expenses: {total[0]}")      

def expense_by_category(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses 
        where Username=?
        GROUP BY category
    """,(username,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No expenses recorded yet.")
    else:
        print("Spend by category:")
        for category, total in rows:
            print(f"  {category}: {total}")
    return rows

def show_table(username):
    conn= create_connection()
    cursor= conn.cursor()
    cursor.execute("select * from expenses where username=?",(username,))
    rows=cursor.fetchall()
    for row in rows :
        print(row)
    conn.close()  


if __name__ == "__main__":
    create_table()
    print("Database and table created successfully.")
    username=input('Enter your username : ') 
    add_expense(username)
    total_expense(username)
    expense_by_category(username)
    show_table(username)
