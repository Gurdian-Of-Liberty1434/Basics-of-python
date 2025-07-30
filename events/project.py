from tkinter import *
root=Tk()
root.title("Length Converter")
root.geometry("400x400")

frame=Frame(master=root,height=400,width=400,bg="light blue")
lbl1=Label(master=frame,text="Enter the length in inches",font=("Arial", 18),bg="light blue")
lbl2=Label(master=frame,text="Length in cm",font=("Arial", 18),bg="light blue")
txt1=Entry(master=frame,font=("Arial", 18))
lbl1.pack()
txt1.pack()
lbl2.pack()
frame.pack()

def convert():
    a=int(txt1.get())
    b=a*2.54
    lbl2.config(text=b)

btn=Button(master=frame,text="Convert",font=("Arial", 18),command=convert)
btn.pack()

root.mainloop()