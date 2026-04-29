import argparse
from commands import add_expense, delete_expense, summary, show_expenses
from utils import valid_month

def dispatch(storage):
    parser = argparse.ArgumentParser(description='Expense Tracker')
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new expense")
    add_parser.add_argument('-d', '--description', help="Description of the expense", required=True, type=str,
                            metavar='')
    add_parser.add_argument('-a', '--amount', help="Expended amount", required=True, type=float, metavar='')
    add_parser.set_defaults(func=lambda args: add_expense(args.description, args.amount, storage))

    list_parser = subparsers.add_parser("list", help='List all expenses')
    list_parser.set_defaults(func=lambda args: show_expenses(storage))

    summary_parser = subparsers.add_parser("summary", help="Show total expenses")
    summary_parser.add_argument('-m', '--month', help="display the total of expenses", type=valid_month, metavar='')
    summary_parser.set_defaults(func=lambda args: summary(storage, args.month))

    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    delete_parser.add_argument('--id', help="Delete the expenses with the id specified", type=int, metavar='',
                               required=True)
    delete_parser.set_defaults(func=lambda args: delete_expense(args.id, storage))

    args = parser.parse_args()
    args.func(args)
