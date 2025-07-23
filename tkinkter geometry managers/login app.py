#Write a program using the Tkinter library to create a Login Application for users.
from tkinter import *
root=Tk()
root.title("Login Application")
root.geometry("400x400")

frame=Frame(master=root,height=400,width=400,bg="light blue")
lbl1=Label(master=frame,text="Username",font=("Arial", 18),bg="light blue")
lbl2=Label(master=frame,text="Password",font=("Arial", 18),bg="light blue")
txt1=Entry(master=frame,font=("Arial", 18))
