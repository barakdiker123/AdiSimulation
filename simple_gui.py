class DF:
    name="non"
    score=0.1
    ph_cognitive = None
    ph_heuristic = None

    def generic_cognitive(self):
        print("This is a generic cognitive message written by" , self.name)

    def generic_heuristic(self):
        print("This is a generic cognitive message written by" , self.name)

    def __lt__(self, other):
         return self.score < other.score

    def print_messages(self):
        if(self.ph_cognitive != None):
            print(self.name, end ="")
            self.ph_cognitive()
        if(self.ph_heuristic != None):
            print(self.name, end ="")
            self.ph_heuristic()
        self.generic_cognitive()
        self.generic_heuristic()
        print()

from tkinter import *
from tkinter import ttk
my_data_vector = []
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Enter Person Specs !").grid(column=0, row=0)
#ttk.Combobox(frm , text="barak").grid(column=2 , row=0)
ttk.Label(frm, text="Enter Name").grid(column=0, row=1)
name_client = ttk.Entry(frm )
name_client.grid(column=1 , row=1)
ttk.Label(frm, text="Enter Score").grid(column=0, row=2)
score_client = ttk.Entry(frm)
score_client.grid(column=1 , row=2)
ttk.Label(frm, text="Phenotype").grid(column=0, row=3)
is_phenotype = ttk.Combobox(frm , values=["Yes","No"])
is_phenotype.grid(column=1, row=3)
def add_field():
    new_df = DF()
    new_df.name = name_client.get()
    new_df.score = float(score_client.get())
    if("Yes" == is_phenotype.get()):
        new_df.ph_cognitive = lambda : print(". ph_cognitive")
        new_df.ph_heuristic = lambda : print(". ph_heuristic")
    my_data_vector.append(new_df)
    name_client.delete(0,'end')
    score_client.delete(0,'end')
ttk.Button(frm, text="Added DF", command=add_field).grid(column=1, row=4)
def display():
    my_data_vector.sort(reverse=True)
    for elem_df in my_data_vector:
        elem_df.print_messages()
ttk.Button(frm, text="Display", command=display).grid(column=0, row=4)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)
root.mainloop()


