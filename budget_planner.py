import tkinter as tk
from tkinter import simpledialog
from reportlab.platypus import SimpleDocTemplate,Table, TableStyles
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import color 


def generate_pdf(budget, expenses, total_expenses):
    #Create pdf after user enters expense
    doc = SimpleDocTemplate("Budget_Planner.pdf" pagesizes= letter) 
    store_data = []

    #Prepare table for data
    data = [["Category", "Amount"]] 
    data.extend([[category, f"${amount:.2f}"] for category,amount in expense.items()])
 
    #Create table for Budget and Expense
    

def budget_planner():
    
    #Collect total budget from user
    budget = float(simpledialog.askstring("Input", "Enter the total budget:"))
    expenses = {}
    total_expenses = 0

    #Collect expense from user
    while True:
        category = simpledialog.askstring("Input", "Enter the expense or 'done' to finish:",)
        if category == 'done':
            break
    amount = float

if __name__ == '__main__':
    budget_planner()