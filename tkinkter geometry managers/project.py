import tkinter as tk
from datetime import datetime

def calculate_age():
    dob = entry_dob.get()
    dob_date = datetime.strptime(dob, "%d/%m/%Y")
    today = datetime.today()
    age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
    label_age.config(text=f"Age: {age} years")

root = tk.Tk()
root.title("Age Calculator")

label_dob = tk.Label(root, text="Date of Birth (dd/mm/yyyy):")
label_dob.grid(row=0, column=0, padx=5, pady=5)

entry_dob = tk.Entry(root, width=20)
entry_dob.grid(row=0, column=1, padx=5, pady=5)

button_calculate = tk.Button(root, text="Calculate Age", command=calculate_age)
button_calculate.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

label_age = tk.Label(root, text="Age: ")
label_age.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()