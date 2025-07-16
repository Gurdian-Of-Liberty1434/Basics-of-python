from tkinter import *
window = Tk()
window.title("Tkinter Sample Window")
window.geometry("400x500")
def click_me():
    label.config(text="Hello " + name.get())

label = Label(window, text="Enter your name")
label.grid(row=0, column=0)

name = Entry(window)
name.grid(row=1, column=0)

button = Button(window, text="Click Me", command=click_me)
button.grid(row=2, column=0)

window.mainloop()