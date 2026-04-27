from utils import is_expenses, compare_months
from datetime import datetime

def add_expense(description, amount, storage):
    expense_id = storage.add(description, amount)
    print(f"Expense added successfully (ID: {expense_id})")

def show_expenses(storage):
    expenses = storage.get_all()

    if not is_expenses(expenses):
        print("No expenses found")
        return

    print(f"{'ID':<4}{'Date':<12}{'Description':<15}{'Amount':>8}")

    for expense in expenses:
        print(f"{expense["id"]:<4}{expense["date"]:<12}{expense["description"]:<15}{"$" + str(expense["amount"]):>8}")


def summary(storage, target_month=None):
    expenses = storage.get_all()

    if not is_expenses(expenses):
        print("No expenses found")
        return

    total_expenses = 0

    for expense in expenses:
        expense_date = datetime.strptime(expense["date"], "%Y-%m-%d")
        expense_month = expense_date.month  # ← this is the key

        if target_month is None or target_month == expense_month:
            total_expenses += expense["amount"]

    print(f"Total expenses: ${total_expenses}")

def delete_expense(expense_id, storage):
    success = storage.delete(expense_id)
    if success:
        print(f"Expense deleted successfully")
    else:
        print("Expense not found")