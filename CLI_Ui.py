from colorama import Fore, Style, init
from tabulate import tabulate
from Finance_Service import FinanceService
from datetime import datetime
from utils import Validation

# Initialize colorama
init(autoreset=True)


class CashFlow:
    
    def __init__(self):
        self.manager = FinanceService()
        self.validation = Validation()
    
    # Add income
    def add_income(self):
        
        print("--- Add Income ---")
        
        print(Fore.CYAN + "Press Enter to use the default category (Salary), or type your own category.")
        while True:
            category = input("Category: ").strip()
            if not category:
                category = "Salary"
            
            if len(category) <= 2 or not category.isalpha():
                print(Fore.RED + "Category must be at least 2 characters long and contain only letters.")
                continue
            break 
        
        data = self.validation.get_transaction_input()
        if not data:
            return
                    
        amount, date = data
        self.manager.add_income(amount, category, date )
        print(Fore.GREEN + "Income added successfully!")
     
     # add expense   
    def add_expense(self):
        
        print("--- Add Expense ---")
        
        while True:
            category = input("Category: ").strip()
            if not category:
                print(Fore.RED + "Category cannot be empty!")
                continue
            
            if len(category) <= 2 or not category.isalpha():
                print(Fore.RED + "Category must be at least 2 characters long and contain only letters.")
                continue
            break
        
        data = self.validation.get_transaction_input()
        if not data:
            return
        
        amount, date = data
        
        self.manager.add_expense(amount, category, date)
        print(Fore.GREEN + "Expense added successfully!")
    
    # View transactions
    def view_transactions(self):
        
        data = self.manager.view_transactions()
        
        if not data:
            print("No transactions found!")
            return
        
        table = [[entry["id"], entry["category"], entry["amount"], entry["date"]] for entry in data]
        print("\n" + tabulate(table, headers=["ID", "Category", "Amount", "Date"], tablefmt="fancy_grid"))
        
    #search transactions method
    def search_transactions(self):
        query = input("\nEnter Category/Date(DD-MM-YYYY): ").strip()
        if not query:
            return
        
        self.validation.sort_transaction(query)
        
     #delete transaction method
    def delete_transaction(self):
        while True:
            query = input("\nEnter a category/date (DD-MM-YYYY) to find the transaction you want to delete: ").strip()
            
            if  self.validation.sort_transaction(query):
                break
                
        try:
            id = int(input("\nEnter Transaction ID to delete: "))
            if self.manager.delete_transaction(id):
                print(Fore.GREEN + f"Transaction {id} deleted.")
            else:
                print(Fore.RED + "Transaction ID not found.")
        except ValueError:
            print(Fore.RED + "Invalid ID.")
    
    # update transaction method        
    def update_transaction(self):
        while True:
            query = input("\n1.Income\n2.Expense\nEnter type to find the transaction you want to update: ").strip()
            if query == "1" or query == "income":
                query = "income"
            elif query == "2" or query == "expense":
                query = "expense"
            else:
                print(Fore.RED + "Invalid input. Please enter '1' for Income or '2' for Expense.")
                continue
            if  self.validation.sort_transaction(query):
                break
        
        try:
            id = int(input("\nEnter Transaction ID to update: "))
            if not any(entry["id"] == id for entry in self.manager.view_transactions()):
                print(Fore.RED + "Transaction ID not found.")
                return
            
            # amount_input = input("New Amount (leave blank to keep current): ").strip()
            category_input = input("New Category (leave blank to keep current): ").strip()
            # date_input = input("New Date (DD-MM-YYYY, leave blank to keep current): ").strip()
            
            data = self.validation.get_transaction_input()
            amount_input, date_input = data if data else (None, None)
            amount = float(amount_input) if amount_input else None
            category = category_input if category_input else None
            date = date_input if date_input else None
            
            if self.manager.update_transaction(id, amount, category, date):
                print(Fore.GREEN + f"Transaction {id} updated.")
            else:
                print(Fore.RED + "Transaction ID not found.")
        except ValueError:
            print(Fore.RED + "Invalid input.")
        
    #view summary report method
    def view_summary_report(self):
        summary = self.manager.get_summary()
        if not summary:
            print("No transactions found!")
            return
        
        total_income = summary["total_income"]
        total_expenses = summary["total_expenses"]
        balance = summary["balance"]
        
        print("\n--- Summary Report ---")
        print(f"Total Income: {Fore.GREEN}${total_income:.2f}")
        print(f"Total Expenses: {Fore.RED}${-total_expenses:.2f}")
        print(f"Net Balance: {Fore.BLUE}${balance:.2f}")
        
        
        