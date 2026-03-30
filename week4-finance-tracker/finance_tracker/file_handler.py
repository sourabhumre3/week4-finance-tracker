import json
import os
import shutil

FILE = "data/expenses.json"
BACKUP = "data/backup/expenses_backup.json"

def save(expenses):
    with open(FILE, "w") as f:
        json.dump([e.to_dict() for e in expenses], f, indent=4)

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def backup():
    shutil.copy(FILE, BACKUP)
    print("Backup created!")

def restore():
    if os.path.exists(BACKUP):
        shutil.copy(BACKUP, FILE)
        print("Data restored!")