
import math
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
#my_data_vector = []
#is_go_on = True
#while is_go_on:
#    new_df = DF()
#    new_df.name = input("What is the Decision Factor's name? : \n")
#    new_df.score = float(input("What is the Score of the new decision factor ? : \n"))
#    is_phenotype = input("Is phenotype Exists ? (yes/no) \n")
#    if(is_phenotype == "yes"):
#        new_df.ph_cognitive = lambda : print(". ph_cognitive")
#        new_df.ph_heuristic = lambda : print(". ph_heuristic")
#    should_perceed = input("Do you have another Decision Factor to enter ?(yes/no) \n")
#    my_data_vector.append(new_df)
#    if(should_perceed == "yes"):
#        is_go_on = True
#    elif(should_perceed == "no"):
#        is_go_on = False
#    else:
#        is_go_on = False
#
#
#my_data_vector.sort(reverse=True)
#for elem_df in my_data_vector:
#    elem_df.print_messages()
#
#print("The number of Total Permutation is ", math.factorial(len(my_data_vector)))
