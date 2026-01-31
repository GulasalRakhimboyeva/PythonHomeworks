# =====================================================
# TASK 1: Library Management System with Custom Exceptions
# =====================================================

# ---------- Custom Exceptions ----------
class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass


# ---------- Book Class ----------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}"


# ---------- Member Class ----------
class Member:
    MAX_BOOKS = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


# ---------- Library Class ----------
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        raise BookNotFoundException(f"Book '{title}' not found")

    def borrow_book(self, member, title):
        book = self.find_book(title)

        if book.is_borrowed:
            raise BookAlreadyBorrowedException(f"Book '{title}' is already borrowed")

        if len(member.borrowed_books) >= Member.MAX_BOOKS:
            raise MemberLimitExceededException("Member has reached borrowing limit")

        book.is_borrowed = True
        member.borrowed_books.append(book)
        print(f"{member.name} borrowed '{title}'")

    def return_book(self, member, title):
        for book in member.borrowed_books:
            if book.title == title:
                book.is_borrowed = False
                member.borrowed_books.remove(book)
                print(f"{member.name} returned '{title}'")
                return
        raise BookNotFoundException(f"{member.name} does not have '{title}'")


# ---------- Task 1 Testing ----------
print("\n--- TASK 1: Library System ---")

library = Library()

library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("Clean Code", "Robert C. Martin"))
library.add_book(Book("Python Basics", "John Doe"))

alice = Member("Alice")
library.add_member(alice)

try:
    library.borrow_book(alice, "1984")
    library.borrow_book(alice, "Clean Code")
    library.borrow_book(alice, "Python Basics")
except Exception as e:
    print("Error:", e)

library.return_book(alice, "1984")


# =====================================================
# TASK 2: Student Grades Management (CSV)
# =====================================================

import csv
from collections import defaultdict

print("\n--- TASK 2: Student Grades ---")

# Create grades.csv
with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Subject", "Grade"])
    writer.writerow(["Alice", "Math", 85])
    writer.writerow(["Bob", "Science", 78])
    writer.writerow(["Carol", "Math", 92])
    writer.writerow(["Dave", "History", 74])

grades = []

# Read grades.csv
with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Grade"] = int(row["Grade"])
        grades.append(row)

# Calculate averages
subject_grades = defaultdict(list)

for entry in grades:
    subject_grades[entry["Subject"]].append(entry["Grade"])

averages = {
    subject: sum(scores) / len(scores)
    for subject, scores in subject_grades.items()
}

# Write average_grades.csv
with open("average_grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg in averages.items():
        writer.writerow([subject, avg])

print("average_grades.csv created successfully")


# =====================================================
# TASK 3: JSON Handling
# =====================================================

import json

print("\n--- TASK 3: JSON Tasks ---")

# Create tasks.json
tasks_data = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]

with open("tasks.json", "w") as file:
    json.dump(tasks_data, file, indent=4)

# Load tasks.json
with open("tasks.json", "r") as file:
    tasks = json.load(file)

# Display tasks
for task in tasks:
    print(f"ID: {task['id']}, Task: {task['task']}, "
          f"Completed: {task['completed']}, Priority: {task['priority']}")

# ---------- Statistics ----------
def calculate_stats(tasks):
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    avg_priority = sum(t["priority"] for t in tasks) / total

    print("\nTask Statistics:")
    print("Total tasks:", total)
    print("Completed tasks:", completed)
    print("Pending tasks:", pending)
    print("Average priority:", avg_priority)

calculate_stats(tasks)

# Modify a task
tasks[0]["completed"] = True

# Save back to JSON
with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)

# Convert JSON to CSV
with open("tasks.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Task", "Completed", "Priority"])
    for task in tasks:
        writer.writerow([
            task["id"],
            task["task"],
            task["completed"],
            task["priority"]
        ])

print("tasks.csv created successfully")
