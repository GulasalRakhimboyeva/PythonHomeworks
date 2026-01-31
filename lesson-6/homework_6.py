# ### Zero Check Decorator

# Write a decorator function called `check` that verifies that the
#  denominator is not equal to 0 and apply it to the following function:

# python
# @check
# def div(a, b):
#    return a / b



# input: div(6, 2)
# output: 3



# input: div(6, 0)
# output: "Denominator can't be zero"
# solution

def check(func):
   def wrapper(a, b):
      if b==0:
         return"Denominator can't be zero"
      
      return func(a, b)
   return wrapper

    
@check
def div(a,b):
    return a/b

print(div(6, 4))
# ---

# ### **Employee Records Manager**
# **Objective**: Create a program to manage employee records using file
#  handling.  

# **Tasks**:  
# 1. **File Creation and Data Entry**  
#    - Create a file named **"employees.txt"**.  
#    - Allow the user to add new employee records.
#  Each record should have the following fields:  
     
#      Employee ID, Name, Position, Salary
     
#      Example of a record:  
     
#      1001, John Doe, Software Engineer, 75000
     

# 2. **Menu Options**  
#    Your program should present the following options:  
   
#    1. Add new employee record
#    2. View all employee records
#    3. Search for an employee by Employee ID
#    4. Update an employee's information
#    5. Delete an employee record
#    6. Exit
   

# 3. **Functional Requirements**  
#    - **Option 1**: Append a new employee record to **"employees.txt"**.  
#    - **Option 2**: Display all employee records from **"employees.txt"**.  
#    - **Option 3**: Allow the user to search for an employee by **Employee ID** and display their details.  
#    - **Option 4**: Update an employee’s information (name, position, or salary) based on the Employee ID.  
#    - **Option 5**: Delete an employee's record from the file using the Employee ID.  
#    - **Option 6**: Exit the program. 
# solution
FILE_NAME = "employees.txt"


def add_employee():
    with open(FILE_NAME, "a") as file:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        file.write(f"{emp_id}, {name}, {position}, {salary}\n")
    print("Employee record added successfully.")


def view_employees():
    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()
            if not records:
                print("No employee records found.")
            else:
                print("\nEmployee Records:")
                for record in records:
                    print(record.strip())
    except FileNotFoundError:
        print("No employee file found.")


def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    found = False
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                if line.startswith(emp_id + ","):
                    print("Employee Found:")
                    print(line.strip())
                    found = True
                    break
        if not found:
            print("Employee not found.")
    except FileNotFoundError:
        print("No employee file found.")


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    updated = False
    records = []

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        with open(FILE_NAME, "w") as file:
            for line in records:
                if line.startswith(emp_id + ","):
                    print("Enter new details:")
                    name = input("New Name: ")
                    position = input("New Position: ")
                    salary = input("New Salary: ")
                    file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                    updated = True
                else:
                    file.write(line)

        if updated:
            print("Employee record updated successfully.")
        else:
            print("Employee not found.")

    except FileNotFoundError:
        print("No employee file found.")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    deleted = False
    records = []

    try:
        with open(FILE_NAME, "r") as file:
            records = file.readlines()

        with open(FILE_NAME, "w") as file:
            for line in records:
                if not line.startswith(emp_id + ","):
                    file.write(line)
                else:
                    deleted = True

        if deleted:
            print("Employee record deleted successfully.")
        else:
            print("Employee not found.")

    except FileNotFoundError:
        print("No employee file found.")


def menu():
    while True:
        print("\n--- Employee Records Manager ---")
        print("1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
menu()

# ---

# ### **Word Frequency Counter**
# **Objective**: Analyze a text file and count how often each word appears.  

# **Tasks**:  
# 1. **File Input**  
#    - Use the file **"sample.txt"**. The file can contain any text (like a paragraph or an article).  
#    - If **"sample.txt"** does not exist, prompt the user to create it by typing in a paragraph.  

# 2. **Count Word Frequency**  
#    - Read the file content and split it into individual words.  
#    - Count the frequency of each word (ignore capitalization, e.g., "The" and "the" should be counted as the same word).  
#    - Ignore punctuation (like commas, periods, etc.).  

# 3. **Output**  
#    - Display the total number of words in the file.  
#    - Display the top 5 most common words with their counts.  
#    - Save the output to a new file called **"word_count_report.txt"**.  

# 4. **Example Output**  
#    **Content of sample.txt**:  
   
#    This is a simple file.
#    This file, is for testing purposes. It is a test file.
   

#    **Console Output**:  
   
#    Total words: 14
#    Top 5 most common words:
#    is - 3 times
#    this - 2 times
#    file - 3 times
#    a - 2 times
#    test - 1 time
   

#    **Content of word_count_report.txt**:  
   
#    Word Count Report
#    Total Words: 14
#    Top 5 Words:
#    is - 3
#    file - 3
#    this - 2
#    a - 2
#    test - 1
   

# **Bonus Task**:  
# - Allow the user to specify how many "top common words" to display (e.g., top 3, top 10, etc.).  
# - Make sure the program ignores case, punctuation, and handles large files efficiently.

# solution

import os
import string
from collections import Counter


FILE_NAME = "sample.txt"
REPORT_FILE = "word_count_report.txt"


def create_file_if_missing():
    if not os.path.exists(FILE_NAME):
        print(f'"{FILE_NAME}" not found.')
        print("Please enter a paragraph to create the file:")
        text = input("> ")
        with open(FILE_NAME, "w") as file:
            file.write(text)
        print(f'"{FILE_NAME}" created successfully.\n')


def read_and_process_file():
    with open(FILE_NAME, "r") as file:
        text = file.read().lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()
    return words


def generate_report(words, top_n):
    total_words = len(words)
    word_counts = Counter(words)
    most_common = word_counts.most_common(top_n)

    # Console output
    print(f"\nTotal words: {total_words}")
    print(f"Top {top_n} most common words:")
    for word, count in most_common:
        print(f"{word} - {count} time(s)")

    # Save to file
    with open(REPORT_FILE, "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write(f"Top {top_n} Words:\n")
        for word, count in most_common:
            file.write(f"{word} - {count}\n")

    print(f"\nReport saved to '{REPORT_FILE}'")


def main():
    create_file_if_missing()
    words = read_and_process_file()

    if not words:
        print("The file is empty.")
        return

    try:
        top_n = int(input("How many top common words would you like to see? "))
    except ValueError:
        print("Invalid input. Showing top 5 words by default.")
        top_n = 5

    generate_report(words, top_n)


# Run the program
main()
