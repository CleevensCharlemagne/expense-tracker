from datetime import datetime

def is_expenses(expenses):
    if expenses:
        return True
    return False

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

def valid_month(value):
    import argparse
    ivalue = int(value)
    if ivalue < 1 or ivalue > 12:
        raise argparse.ArgumentTypeError("Month must be between 1 and 12")
    return ivalue
