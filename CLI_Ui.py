
import sys
from colorama import Fore, Style, init
from tabulate import tabulate
from Finance_Service import FinanceService
import os

# Initialize colorama
init(autoreset=True)


class CashFlow:
    
    def __init__(self):
        self.manager = FinanceService()
    
    # Add income
    def add_income(self):
        
        print("--- Add Income ---")
        
        amount = float(input("Amount: "))
        category = input("Category: ").strip()
        date = input("Date (DD-MM-YYYY): ").strip()
        
        if not amount or not category or not date:
            print("All fields are required!")
            return
        
        self.manager.add_income(amount, category, date)
        print(Fore.GREEN + "Income added successfully!")
     
     # add expense   
    def add_expense(self):
        
        print("--- Add Expense ---")
        
        amount = float(input("Amount: "))
        category = input("Category: ").strip()
        date = input("Date (DD-MM-YYYY): ").strip()
        
        if not amount or not category or not date:
            print("All fields are required!")
            return
        
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
        
        results = self.manager.search_transactions(query)
        if not results:
            print(Fore.RED + "No results found.")
            return
        
        table = [[entry["id"], entry["category"], entry["amount"], entry["date"]] for entry in results]
        print("\n" + tabulate(table, headers=["ID", "Category", "Amount", "Date"], tablefmt="fancy_grid"))   
        
     #delete transaction method
    def delete_transaction(self):
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
        try:
            id = int(input("\nEnter Transaction ID to update: "))
            if not any(entry["id"] == id for entry in self.manager.view_transactions()):
                print(Fore.RED + "Transaction ID not found.")
                return
            
            amount_input = input("New Amount (leave blank to keep current): ").strip()
            category_input = input("New Category (leave blank to keep current): ").strip()
            date_input = input("New Date (DD-MM-YYYY, leave blank to keep current): ").strip()
            
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
        # print(f"Total Income: {Fore.GREEN}${total_income:.2f}")
        # print(f"Total Expenses: {Fore.RED}${-total_expenses:.2f}")
        # print(f"Net Balance: {Fore.BLUE}${balance:.2f}")
        
        income_color = f"{Fore.GREEN}${total_income:.2f}"
        expense_color = f"{Fore.RED}${-total_expenses:.2f}"
        balance_color = f"{Fore.BLUE}${balance:.2f}"
        
        table = [
            ["Total Income", income_color],
            ["Total Expenses", expense_color],
            ["Net Balance", balance_color]
        ]
        print("\n" + tabulate(table, headers=["Description", "Amount"], tablefmt="fancy_grid"))
        