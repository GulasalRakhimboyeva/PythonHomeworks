# =========================================================
# PART 1: Generalized Vector Class
# =========================================================

import math
import os
import json
from abc import ABC, abstractmethod


class Vector:
    def __init__(self, *components):
        if not components:
            raise ValueError("Vector must have at least one component")
        self.components = tuple(components)

    def __str__(self):
        return f"Vector{self.components}"

    def __len__(self):
        return len(self.components)

    def _check_dimension(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same dimension")

    def __add__(self, other):
        self._check_dimension(other)
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        self._check_dimension(other)
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            self._check_dimension(other)
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*[a * other for a in self.components])
        else:
            raise TypeError("Unsupported operand")

    def __rmul__(self, scalar):
        return self * scalar

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector(*[round(a / mag, 3) for a in self.components])


# =========================================================
# PART 2: Employee Records Manager (OOP)
# =========================================================

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"

    @staticmethod
    def from_string(line):
        emp_id, name, position, salary = line.strip().split(", ")
        return Employee(emp_id, name, position, salary)


class EmployeeManager:
    FILE_NAME = "employees.txt"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            open(self.FILE_NAME, "w").close()

    def _read_all(self):
        with open(self.FILE_NAME, "r") as file:
            return [Employee.from_string(line) for line in file if line.strip()]

    def _write_all(self, employees):
        with open(self.FILE_NAME, "w") as file:
            for emp in employees:
                file.write(str(emp) + "\n")

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        employees = self._read_all()

        if any(emp.employee_id == emp_id for emp in employees):
            print("Employee ID already exists!")
            return

        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")

        employee = Employee(emp_id, name, position, salary)
        with open(self.FILE_NAME, "a") as file:
            file.write(str(employee) + "\n")

        print("Employee added successfully!")

    def view_employees(self):
        employees = self._read_all()
        if not employees:
            print("No records found.")
            return
        print("\nEmployee Records:")
        for emp in employees:
            print(emp)

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")
        for emp in self._read_all():
            if emp.employee_id == emp_id:
                print("Employee Found:")
                print(emp)
                return
        print("Employee not found.")

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        employees = self._read_all()

        for emp in employees:
            if emp.employee_id == emp_id:
                emp.name = input("New Name: ")
                emp.position = input("New Position: ")
                emp.salary = input("New Salary: ")
                self._write_all(employees)
                print("Employee updated successfully!")
                return
        print("Employee not found.")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        employees = self._read_all()
        updated = [emp for emp in employees if emp.employee_id != emp_id]

        if len(updated) == len(employees):
            print("Employee not found.")
        else:
            self._write_all(updated)
            print("Employee deleted successfully!")

    def menu(self):
        while True:
            print("\nEmployee Records Manager")
            print("1. Add Employee")
            print("2. View Employees")
            print("3. Search Employee")
            print("4. Update Employee")
            print("5. Delete Employee")
            print("6. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")


# =========================================================
# PART 3: To-Do Application (Multi-Format, Extensible)
# =========================================================

class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Task(**data)


class Storage(ABC):
    @abstractmethod
    def save(self, tasks):
        pass

    @abstractmethod
    def load(self):
        pass


class JSONStorage(Storage):
    def __init__(self, filename="tasks.json"):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)

    def load(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as file:
            return [Task.from_dict(data) for data in json.load(file)]


class TodoManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = storage.load()

    def add_task(self):
        task = Task(
            input("Task ID: "),
            input("Title: "),
            input("Description: "),
            input("Due Date (optional): "),
            input("Status: ")
        )
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task in self.tasks:
            print(vars(task))

    def update_task(self):
        task_id = input("Enter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = input("New Title: ")
                task.description = input("New Description: ")
                task.due_date = input("New Due Date: ")
                task.status = input("New Status: ")
                print("Task updated!")
                return
        print("Task not found.")

    def delete_task(self):
        task_id = input("Enter Task ID to delete: ")
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        print("Task deleted.")

    def filter_tasks(self):
        status = input("Enter status to filter: ")
        for task in self.tasks:
            if task.status.lower() == status.lower():
                print(vars(task))

    def save_tasks(self):
        self.storage.save(self.tasks)
        print("Tasks saved.")

    def menu(self):
        while True:
            print("\nTo-Do Application")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Update Task")
            print("4. Delete Task")
            print("5. Filter Tasks")
            print("6. Save Tasks")
            print("7. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                self.save_tasks()
            elif choice == "7":
                break
            else:
                print("Invalid choice!")


# =========================================================
# MAIN MENU (OPTIONAL)
# =========================================================

if __name__ == "__main__":
    print("Choose program to run:")
    print("1. Employee Records Manager")
    print("2. To-Do Application")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        EmployeeManager().menu()
    elif choice == "2":
        TodoManager(JSONStorage()).menu()
    else:
        print("Exiting.")
