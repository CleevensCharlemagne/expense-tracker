def add_expense(description, amount, storage):
    expense_id = storage.add(description, amount)
    print(f"Expense added successfully (ID: {expense_id})")


def mark_in_progress(task_id, storage):
    storage.update_status(task_id, "in-progress")
    print(f"Task {task_id} marked as in progress")


def mark_done(task_id, storage):
    storage.update_status(task_id, "done")
    print(f"Task {task_id} marked as done")


def update(task_id, new_title, storage):
    success = storage.update_title(task_id, new_title)
    if success:
        print(f"Task updated successfully (ID: {task_id})")
    else:
        print("Task not found")


def delete(task_id, storage):
    success = storage.delete(task_id)
    if success:
        print(f"Task deleted successfully (ID: {task_id})")
    else:
        print("Task not found")


def show(storage):
    expenses = storage.get_all()

    if not expenses:
        print("No expenses found")
        return

    print(f"{'ID':<4}{'Date':<12}{'Description':<15}{'Amount':>8}")

    for expense in expenses:
        print(f"{expense["id"]:<4}{expense["date"]:<12}{expense["description"]:<15}{expense["amount"]:>8}")