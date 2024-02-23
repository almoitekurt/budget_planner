import tkinter as tk
from tkinter import simpledialog
from reportlab.lib.pagesizes import letter


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