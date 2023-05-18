
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
#ttk.Combobox(frm , text="barak").grid(column=2 , row=0)
ttk.Label(frm, text="Enter Name").grid(column=0, row=1)
ttk.Entry(frm ).grid(column=1 , row=1)
ttk.Label(frm, text="Enter Score").grid(column=0, row=2)
ttk.Entry(frm ).grid(column=1 , row=2)
ttk.Label(frm, text="Phenotype").grid(column=0, row=3)
ttk.Combobox(frm , values=["Yes","No"]).grid(column=1, row=3)
ttk.Button(frm, text="Added DF", command=root.destroy).grid(column=1, row=4)
root.mainloop()

from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
def clicked():
    lbl.configure(text="Button was clicked !!")
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
window.mainloop()
