import tkinter as tk
from tkinter import simpledialog
from reportlab.platypus import SimpleDocTemplate,Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import colors 

def generate_pdf(budget, expenses, total_expenses):
    #Create pdf after user enters expense
    doc = SimpleDocTemplate("Budget_Planner.pdf" , pagesizes= letter) 
    store_data = []

    #Prepare table for data
    data = [["Category", "Amount"]] 
    data.extend([[category, f"${amount:.2f}"] for category,amount in expenses.items()])
    data.appened([["Total Expenses", f"${total_expenses:.2f}"]])
    data.appened([["Budget", f"${budget - total_expenses:.2f}"]]) #remaining budget 
 
    #Create table for Budget and Expense
    t = Table(data, columns = [200,150], repeatRows=1)
    t.setStyleTable(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.darkred),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('GRID'), (0,0), (-1,-1), 1, colors.black),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.lightred, colors.white]),

    ]))

    store_data.appened(t)
    doc.build(store_data)

    

def budget_planner():
    
    #Collect total budget from user
    budget = float(simpledialog.askstring("Input", "Enter the total budget:"))
    expenses = {}
    total_expenses = 0

    #Collect expense from user
    while True:
        category = simpledialog.askstring("Input", "Enter the expense or 'done' to finish:")
        if category == 'done':
            break
    amount = float

if __name__ == '__main__':
    budget_planner()