from utils import print_menu
import math
import matplotlib.pyplot as plt
from services import add_expense, add_income, total_expenses, total_incomes, net_balance
from storage import load_data, save_data
a="    "
b="  "
def run():
    expenses, incomes = load_data() 
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice =="1":
            desc =input("Description about : ")
            amt=float(input("Amount: "))
            cat=input("Category for: " )
            date=input("Date (YYYY-MM-DD): ")
            add_expense   (expenses, desc, amt, cat, date)
        elif choice=="2":
            src = input("Source of: ")
            amt =float(input("Amount in : "))
            date = input("Date (YYYY-MM-DD): ")
            add_income(incomes, src,  amt,  date) 
        elif choice== "3":
            print("Total Expenses of u :", total_expenses(expenses))
            print("Total Income of u :", total_incomes(incomes))
            print("Net Balance of u :", net_balance(expenses, incomes))
        elif choice ==   "0"  :
            save_data(expenses, incomes)
            print("Data saved.. Program ending....")
            break




        else:
            print("Invalid choice, we are sorry . Try again.")

if __name__ == "__main__":
    run()















