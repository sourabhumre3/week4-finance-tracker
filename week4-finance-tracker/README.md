# 💰 Personal Finance Tracker

## 📌 Project Description

Personal Finance Tracker एक Python-based application है जो users को अपने daily expenses track करने में मदद करता है।
इस project की मदद से user अपने खर्चों को add, store और analyze कर सकता है।

यह project file handling, JSON storage, modular coding और error handling concepts को practically implement करता है।

---

## 🎯 Objectives

* Users को expense manage करने में मदद करना
* Data को permanently store करना (JSON file में)
* Monthly खर्च का basic analysis करना
* Python file handling और modules सीखना

---

## ✨ Features

* ➕ Add new expense (date, amount, category, description)
* 📄 View all expenses
* 💾 Save data in JSON file
* 🔄 Load data automatically when program starts
* 📊 Basic report (total expense)
* 🗂 Organized modular code structure
* ⚠ Error handling (file not found, invalid input)

---

## 🛠 Technologies Used

* Python 3
* JSON (for data storage)
* File Handling (read/write)
* Modular Programming

---

## 📁 Project Structure

week4-finance-tracker/
│── finance_tracker/
│   ├── main.py
│   ├── expense.py
│   ├── expense_manager.py
│   ├── file_handler.py
│   ├── reports.py
│   └── utils.py
│
│── data/
│   ├── expenses.json
│   ├── backup/
│   └── exports/
│
│── tests/
│   ├── test_expense.py
│   ├── test_file_handler.py
│   └── test_reports.py
│
│── run.py
│── README.md
│── requirements.txt
│── .gitignore

---

## ⚙️ How to Run the Project

### Step 1: Open Terminal / CMD

Navigate to project folder:

```
cd week4-finance-tracker
```

### Step 2: Run the program

```
python run.py
```

---

## 🖥 Sample Menu

```
1. Add Expense
2. View Expenses
0. Exit
```

---

## 📊 Example Data (expenses.json)

```
[
  {
    "date": "2026-03-30",
    "amount": 200,
    "category": "Food",
    "description": "Lunch"
  }
]
```

---

## 🧪 Testing

* Basic test files included in `tests/` folder
* Program manually tested with different inputs
* File read/write operations verified

---

## ⚠ Error Handling

* File not found handled automatically
* Invalid input handling (amount validation)
* Safe file reading using try-except

---

## 🚀 Future Improvements

* Budget tracking feature
* Monthly/weekly reports
* Graphical visualization
* CSV export feature
* GUI (Tkinter or Web app)

---

## 👨‍💻 Author

Your Name

---

## 📌 Conclusion

यह project Python file handling और real-world application development को समझने के लिए बहुत useful है।
इससे user practical skills सीखता है जो future projects में काम आएंगी।

---
