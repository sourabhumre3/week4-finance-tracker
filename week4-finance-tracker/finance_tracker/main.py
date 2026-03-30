from finance_tracker.expense import Expense
from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.file_handler import save, load, backup, restore
from finance_tracker.reports import monthly_report, category_report
import csv

class FinanceTracker:
    def __init__(self):
        self.manager = ExpenseManager()
        data = load()

        for d in data:
            exp = Expense(d["date"], d["amount"], d["category"], d["description"])
            self.manager.add(exp)

        self.budget = 0

    def run(self):
        while True:
            print("\n========== MENU ==========")
            print("1. Add New Expense")
            print("2. View All Expenses")
            print("3. Search Expenses")
            print("4. Generate Monthly Report")
            print("5. View Category Breakdown")
            print("6. Set/Update Budget")
            print("7. Export Data to CSV")
            print("8. View Statistics")
            print("9. Backup/Restore Data")
            print("0. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view()
            elif choice == "3":
                self.search()
            elif choice == "4":
                monthly_report(self.manager.get_all())
            elif choice == "5":
                category_report(self.manager.category_wise())
            elif choice == "6":
                self.set_budget()
            elif choice == "7":
                self.export_csv()
            elif choice == "8":
                self.stats()
            elif choice == "9":
                self.backup_restore()
            elif choice == "0":
                save(self.manager.get_all())
                print("Saved & Exit")
                break

    def add_expense(self):
        date = input("Date: ")
        amount = float(input("Amount: "))
        category = input("Category: ")
        desc = input("Description: ")

        self.manager.add(Expense(date, amount, category, desc))

    def view(self):
        for e in self.manager.get_all():
            print(e.to_dict())

    def search(self):
        key = input("Search keyword: ")
        result = self.manager.search(key)
        for r in result:
            print(r.to_dict())

    def set_budget(self):
        self.budget = float(input("Enter budget: "))
        print("Budget set!")

    def export_csv(self):
        with open("data/exports/expenses.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Amount", "Category", "Description"])
            for e in self.manager.get_all():
                writer.writerow([e.date, e.amount, e.category, e.description])
        print("Exported to CSV!")

    def stats(self):
        total = self.manager.total()
        print("Total खर्च:", total)
        print("Budget:", self.budget)
        print("Remaining:", self.budget - total)

    def backup_restore(self):
        print("1. Backup")
        print("2. Restore")
        ch = input("Choice: ")

        if ch == "1":
            backup()
        elif ch == "2":
            restore()