import tkinter as tk
from tkinter import messagebox

def check_password_strength():
    password = password_entry.get()
    if len(password) < 8:
        strength_label.config(text="Weak", fg="red")
    elif len(password) < 12:
        strength_label.config(text="Medium", fg="orange")
    else:
        strength_label.config(text="Strong", fg="green")

root = tk.Tk()
root.title("Password Strength Checker")

password_label = tk.Label(root, text="Enter Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*", width=20)
password_entry.pack()

check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack()

strength_label = tk.Label(root, text="")
strength_label.pack()

root.mainloop()