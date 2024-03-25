import tkinter as tk
from tkinter import simpledialog
from reportlab.platypus import SimpleDocTemplate,Table, TableStyle
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors

def generate_pdf(budget, expenses, total_expenses):
    #Create pdf after user enters expense
    doc = SimpleDocTemplate("Budget_Planner.pdf" , pagesizes= letter) 
    story = []

    #Prepare table for data
    data = [["Category", "Amount"]] 
    data.extend([[category, f"${amount:.2f}"] for category,amount in expenses.items()])
    data.append(["Total Expenses", f"${total_expenses:.2f}"])
    data.append(["Budget", f"${budget - total_expenses:.2f}"]) #remaining budget 
 
    #Create table for Budget and Expense
    t = Table(data, colWidths=[200,150], repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.pink),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.lightblue, colors.white]),

    ]))

    story.append(t) #call data to table
    doc.build(story) #build table with stored data that is from input


def budget_planner():
    root = tk.Tk()
    root.withdraw()

    #Collect total budget from user
    budget = float(simpledialog.askstring("Input", "Enter the total budget:", parent=root))
    expenses = {}
    total_expenses = 0

    #Collect expense from user
    while True:
        category = simpledialog.askstring("Input", "Enter the expense or 'done' to finish:", parent=root)
        if category.lower() == 'done':
            break
        amount = float(simpledialog.askstring("Input", f"Enter the amount for {category}:", parent=root))
        expenses[category.capitalize()] = expenses.get(category.capitalize(),0) + amount
        total_expenses += amount

    generate_pdf(budget, expenses,total_expenses)
    tk.messagebox.showinfo("INFO", "Budget planner PDF has been created")

if __name__ == '__main__':
    budget_planner()