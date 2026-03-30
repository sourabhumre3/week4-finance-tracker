class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add(self, expense):
        self.expenses.append(expense)

    def get_all(self):
        return self.expenses

    def search(self, keyword):
        return [e for e in self.expenses if keyword.lower() in e.description.lower()]

    def total(self):
        return sum(e.amount for e in self.expenses)

    def category_wise(self):
        data = {}
        for e in self.expenses:
            data[e.category] = data.get(e.category, 0) + e.amount
        return data