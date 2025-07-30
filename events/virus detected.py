from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Virus Detected")
window.geometry("300x300")
def msg():
    messagebox.showwarning("Alert!","Stop! Virus Detected!")
def msg1():
    messagebox.showerror("Error!","Error found please check code")
def msg2():
    messagebox.showinfo("Info","Display information")

button=Button(window,text="Scan for viruses",command=msg)
button.place(x=48,y=0)
button=Button(window, text="Error message",command=msg1)
button.place(x=48,y=50)
button=Button(window, text="Show info",command=msg2)
button.place(x=48,y=100)
window.mainloop()