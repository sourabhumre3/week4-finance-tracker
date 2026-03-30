def monthly_report(expenses):
    print("\n--- Monthly Report ---")
    total = sum(e.amount for e in expenses)
    print("Total खर्च:", total)

def category_report(data):
    print("\n--- Category Breakdown ---")
    for k, v in data.items():
        print(k, ":", v)