from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window=Tk()
window.title("Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure(1, minsize=100, weight=1)

def openfile():
    filepath=askopenfilename(filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    txt_edit.delete("1.0", END)
    with open(filepath, "r") as input_file:
        text=input_file.read()
        txt_edit.insert("1.0", text)
        window.title(f"Text Editor - {filepath}")

def savefile():
    filepath=asksaveasfilename(defaultextension="txt", filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text=txt_edit.get("1.0", END)
        output_file.write(text)
        window.title(f"Text Editor - {filepath}")

txt_edit=Text(window)
fr_buttons=Frame(window)
btn_open=Button(fr_buttons,text="Open",command=openfile)
btn_save=Button(fr_buttons,text="Save",command=savefile)
btn_open.grid(row=0, column=0, sticky="nsew")
btn_save.grid(row=1, column=0, sticky="nsew")
fr_buttons.grid(row=0, column=0, sticky="nsew")
txt_edit.grid(row=0, column=1, sticky="nsew")
window.mainloop()