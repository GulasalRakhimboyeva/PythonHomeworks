import os 
class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: ${self.balance:.2f}"


class Bank:
    FILE_NAME = "accounts.txt"

    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def generate_account_number(self):
        return str(len(self.accounts) + 1001)

    def create_account(self, name, initial_deposit):
        if initial_deposit < 0:
            print("Initial deposit must be positive.")
            return

        account_number = self.generate_account_number()
        self.accounts[account_number] = Account(account_number, name, initial_deposit)
        self.save_to_file()
        print(f"Account created successfully! Account Number: {account_number}")

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            print(account)
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        account = self.accounts.get(account_number)
        if account:
            account.balance += amount
            self.save_to_file()
            print("Deposit successful.")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if not account:
            print("Account not found.")
            return

        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > account.balance:
            print("Insufficient balance.")
        else:
            account.balance -= amount
            self.save_to_file()
            print("Withdrawal successful.")

    def save_to_file(self):
        with open(self.FILE_NAME, "w") as file:
            for acc in self.accounts.values():
                file.write(f"{acc.account_number},{acc.name},{acc.balance}\n")

    def load_from_file(self):
        if not os.path.exists(self.FILE_NAME):
            return

        with open(self.FILE_NAME, "r") as file:
            for line in file:
                acc_num, name, balance = line.strip().split(",")
                self.accounts[acc_num] = Account(acc_num, name, float(balance))

    def menu(self):
        while True:
            print("\n--- Bank Menu ---")
            print("1. Create Account")
            print("2. View Account")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                name = input("Enter name: ")
                deposit = float(input("Enter initial deposit: "))
                self.create_account(name, deposit)

            elif choice == "2":
                acc_num = input("Enter account number: ")
                self.view_account(acc_num)

            elif choice == "3":
                acc_num = input("Enter account number: ")
                amount = float(input("Enter deposit amount: "))
                self.deposit(acc_num, amount)

            elif choice == "4":
                acc_num = input("Enter account number: ")
                amount = float(input("Enter withdrawal amount: "))
                self.withdraw(acc_num, amount)

            elif choice == "5":
                print("Thank you for using the bank application!")
                break

            else:
                print("Invalid choice.")

a=Bank()
a.menu()