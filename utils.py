from colorama import Fore, Style, init
from datetime import datetime 
from tabulate import tabulate
from Finance_Service import FinanceService

class Validation:
    def __init__(self):
        self.manager = FinanceService()

    # Get the transaction input from the user
    def get_transaction_input(self):
        while True:
            try:
                amount = float(input("Amount: "))
                if amount > 0:
                    break
                else:
                    print(Fore.RED + "Amount cannot be zero or negative!")
            except ValueError:
                print(Fore.RED + "Invalid amount. Please enter a number.")
                continue

        print(Fore.CYAN + "Press Enter to use today's date, or enter a date (DD-MM-YYYY).")
        while True:
            date = input("Date (DD-MM-YYYY): ").strip()
            
            if not date:
                date = datetime.now().strftime("%d-%m-%Y")
                
            if date:
                try:
                    datetime.strptime(date, "%d-%m-%Y")
                    break
                except ValueError:
                    print(Fore.RED + "Invalid date format. Please use DD-MM-YYYY.")

        return amount, date
    
    def sort_transaction(self,query):
        results = self.manager.search_transactions(query)
        if not results:
            print(Fore.RED + "No results found." )
            return
        
        table = [[entry["id"], entry["category"], entry["amount"], entry["date"]] for entry in results]
        print("\n" + tabulate(table, headers=["ID", "Category", "Amount", "Date"], tablefmt="fancy_grid"))
        
        return True
    
    