expenses = [
    {"id": 1, "date": "2024-08-06", "description": "Lunch", "amount": 20},
    {"id": 2, "date": "2024-08-06", "description": "Dinner", "amount": 10},
]

print(f"{'ID':<4}{'Date':<12}{'Description':<15}{'Amount':>8}")

for expense in expenses:
    print(f"{expense["id"]:<4}{expense["date"]:<12}{expense["description"]:<15}{"$"+str(expense["amount"]):>8}")