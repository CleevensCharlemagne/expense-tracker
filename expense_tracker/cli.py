import sys
from expense_tracker.dispatcher import dispatch
from expense_tracker.storage import Storage

def main():
    storage = Storage("expenses.json")
    args = sys.argv[1:]

    if not args:
        print("No command provided")
        return

    dispatch(args, storage)


if __name__ == "__main__":
    main()