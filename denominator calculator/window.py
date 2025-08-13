from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("main")
def topwin():
    toP = Toplevel()
    toP.geometry("180x100")
    toP.title("toplevel")
    Top = Label(toP, text = "This is toplevel window")
    Top.pack()

    toP.mainloop()
TOP = Label(root, text = "This is root window")
btn = Button(root, text = "click here to open another window", command = topwin)


TOP.pack()
btn.pack()