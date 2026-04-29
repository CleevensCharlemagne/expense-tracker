import json
import os
from utils import get_current_date


class Storage:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump([], f)

    def _read(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def _write(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

    def get_all(self):
        return self._read()

    def add(self, description, amount):
        data = self._read()
        expense_id = max([e["id"] for e in data], default=0) + 1

        data.append({
            "id": expense_id,
            "description": description,
            "amount": amount,
            "date": get_current_date()
        })

        self._write(data)
        return expense_id

    def delete(self, expense_id):
        data = self._read()

        new_data = [expense for expense in data if expense["id"] != expense_id]

        if len(data) == len(new_data):
            return False

        self._write(new_data)
        return True