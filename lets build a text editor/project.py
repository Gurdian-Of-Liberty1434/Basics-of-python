#write a python program to create an application to take inputs of the principal amount, time period and rate of interest from the user, and return the simple interest and compound interest on the same principle using the tkinter library
import tkinter as tk
from tkinter import messagebox

class InterestCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Interest Calculator App")

        tk.Label(self.window, text="Principal Amount:").grid(row=0, column=0)
        tk.Label(self.window, text="Time Period (years):").grid(row=1, column=0)
        tk.Label(self.window, text="Rate of Interest (%):").grid(row=2, column=0)

        self.principal_entry = tk.Entry(self.window)
        self.time_entry = tk.Entry(self.window)
        self.rate_entry = tk.Entry(self.window)

        self.principal_entry.grid(row=0, column=1)
        self.time_entry.grid(row=1, column=1)
        self.rate_entry.grid(row=2, column=1)

        tk.Button(self.window, text="Calculate", command=self.calculate_interest).grid(row=3, column=0)
        tk.Button(self.window, text="Reset", command=self.reset_fields).grid(row=3, column=1)

        tk.Label(self.window, text="Simple Interest:").grid(row=4, column=0)
        tk.Label(self.window, text="Compound Interest:").grid(row=5, column=0)

        self.simple_interest_label = tk.Label(self.window, text="")
        self.compound_interest_label = tk.Label(self.window, text="")

        self.simple_interest_label.grid(row=4, column=1)
        self.compound_interest_label.grid(row=5, column=1)

    def calculate_interest(self):
        try:
            principal = float(self.principal_entry.get())
            time = float(self.time_entry.get())
            rate = float(self.rate_entry.get())

            simple_interest = (principal * time * rate) / 100
            compound_interest = principal * (1 + (rate / 100)) ** time - principal

            self.simple_interest_label.config(text=f"{simple_interest:.2f}")
            self.compound_interest_label.config(text=f"{compound_interest:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

    def reset_fields(self):
        self.principal_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.rate_entry.delete(0, tk.END)
        self.simple_interest_label.config(text="")
        self.compound_interest_label.config(text="")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calculator = InterestCalculator()
    calculator.run()