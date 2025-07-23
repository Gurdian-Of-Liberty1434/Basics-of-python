#Create a root window that contains a number pad similar to a phone dialer using the Python Tkinter library

from tkinter import *
root=Tk()
root.title("Number Pad")
root.geometry("250x300")
nums=[[1,2,3],[4,5,6],[7,8,9],['#',0,'*']]
for i in range(4):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
for i in range(4):
    for j in range(3):
        frame=Frame(
            master=root,
            relief=SUNKEN,
            borderwidth=1,
            bg="light blue"
        )
        frame.grid(row=i,column=j,sticky="nsew")
        
        label=Label(master=frame,text=nums[i][j],font=("Arial", 18),bg="light blue")
        label.pack(expand=True, fill='both', padx=5, pady=5)

root.mainloop()