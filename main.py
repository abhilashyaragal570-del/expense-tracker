import json
import datetime


class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = []
        self.load()

    def load(self):
        try:
            with open(self.filename, "r") as f:
                self.expenses = json.load(f)
        except FileNotFoundError:
            self.expenses = []

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.expenses, f, indent=2)

    def add(self, name, amount, category):
        self.expenses.append({
            "name": name,
            "amount": amount,
            "category": category.strip().title(),
            "date": str(datetime.date.today())
        })
        self.save()

    def totals_by_category(self):
        totals = {}
        for e in self.expenses:
            category = e["category"]
            totals[category] = totals.get(category, 0) + e["amount"]
        return totals

    def delete(self, index):
        self.expenses.pop(index)
        self.save()


def get_amount():
    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                print("Amount must be more than 0.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")


def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add expense")
        print("2. View all expenses")
        print("3. Total per category")
        print("4. Delete an expense")
        print("5. Exit")
        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            amount = get_amount()
            category = input("Category: ")
            tracker.add(name, amount, category)
            print("Expense added.")
        elif choice == "2":
            if not tracker.expenses:
                print("No expenses yet.")
            for i, e in enumerate(tracker.expenses, start=1):
                print(i, e["name"], e["amount"], e["category"], e.get("date", ""))
        elif choice == "3":
            if not tracker.expenses:
                print("No expenses yet.")
            for category, total in tracker.totals_by_category().items():
                print(f"{category}: {total}")
        elif choice == "4":
            if not tracker.expenses:
                print("No expenses yet.")
            else:
                for i, e in enumerate(tracker.expenses, start=1):
                    print(i, e["name"], e["amount"])
                try:
                    number = int(input("Delete which number? "))
                    if 1 <= number <= len(tracker.expenses):
                        tracker.delete(number - 1)
                        print("Deleted.")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()