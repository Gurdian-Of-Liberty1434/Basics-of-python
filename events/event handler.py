from tkinter import *

window=Tk()
window.title("Events")
window.geometry("100x100")
def handle_click(event):
    print("\nbutton is clicked")

button=Button(text="Click Me")
button.pack()

button.bind("<Button-1>", handle_click)
window.mainloop()