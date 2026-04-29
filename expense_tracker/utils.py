from datetime import datetime

def is_expenses(expenses):
    if expenses:
        return True
    return False

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")
