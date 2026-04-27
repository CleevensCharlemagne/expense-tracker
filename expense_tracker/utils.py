from datetime import datetime

def is_expenses(expenses):
    if expenses:
        return True
    return False

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

def compare_months(expense, target_month):
    if expense['date'].month == target_month:
        return True
    return False
