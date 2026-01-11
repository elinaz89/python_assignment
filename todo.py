# ==========================================
# Simple To-Do List Application
# Author: Elnaz MOHAMMADZADEH ROSHTKHARI
# Description:
# - Add tasks
# - Mark tasks as done / undone
# - Save tasks to CSV
# - Show simple diagram using matplotlib
# ==========================================

import csv
from datetime import date
import matplotlib.pyplot as plt

FILE_NAME = "tasks.csv"

# ------------------------------------------
# Load tasks from CSV file
# ------------------------------------------
def load_tasks():
    tasks = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header
            for row in reader:
                if len(row) >= 3:
                    tasks.append({
                        "task": row[0],
                        "created": row[1],
                        "done": int(row[2])
                    })
    except FileNotFoundError:
        pass  # Start with empty list if file does not exist
    return tasks

# ------------------------------------------
# Save tasks to CSV file
# ------------------------------------------
def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["task", "created", "done"])
        for t in tasks:
            writer.writerow([t["task"], t["created"], t["done"]])

# ------------------------------------------
# List all tasks with status
# ------------------------------------------
def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, start=1):
        mark = "✓" if t["done"] == 1 else " "
        print(f"{i}. [{mark}] {t['task']} (created: {t['created']})")

# ------------------------------------------
# Add new task(s)
# Supports single or comma-separated input
# ------------------------------------------
def add_task(tasks):
    text = input("Enter task(s) (comma-separated allowed): ").strip()
    if not text:
        return
    for t in text.split(","):
        tasks.append({
            "task": t.strip(),
            "created": str(date.today()),
            "done": 0
        })
    print("Task(s) added.")

# ------------------------------------------
# Update task status (done / undone)
# Supports single or multiple numbers
# ------------------------------------------
def update_status(tasks):
    if not tasks:
        print("No tasks to update.")
        return

    list_tasks(tasks)
    raw = input("Task number(s) (e.g. 2 or 1,3): ").strip()
    for p in raw.split(","):
        if p.strip().isdigit():
            i = int(p.strip()) - 1
            if 0 <= i < len(tasks):
                tasks[i]["done"] = 0 if tasks[i]["done"] == 1 else 1
    print("Status updated.")

# ------------------------------------------
# Show simple diagram (done vs open tasks)
# ------------------------------------------
def show_diagram(tasks):
    done = sum(t["done"] for t in tasks)
    open_tasks = len(tasks) - done
    plt.bar(["Done", "Open"], [done, open_tasks])
    plt.title("Task Status Overview")
    plt.ylabel("Number of Tasks")
    plt.show()

# ------------------------------------------
# Main menu
# ------------------------------------------
def menu():
    tasks = load_tasks()
    while True:
        print("\n=== TO-DO MENU ===")
        print("1) Add task")
        print("2) List tasks")
        print("3) Save & Exit")
        print("4) Update status (done/undo)")
        print("5) Show diagram")

        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            save_tasks(tasks)
            print("Saved. Goodbye!")
            break
        elif choice == "4":
            update_status(tasks)
        elif choice == "5":
            show_diagram(tasks)
        else:
            print("Invalid choice.")

# ------------------------------------------
# Program start
# ------------------------------------------
menu()
