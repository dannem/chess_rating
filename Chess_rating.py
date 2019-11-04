
# coding: utf-8

def main():
    # Create the entire GUI program
    program = RatingGui()

    # Start the GUI event loop
    program.window.mainloop()

from tkinter import Tk, Label, Button, Toplevel, TOP, Y, LEFT, RIGHT, messagebox
from tkinter import ttk
class RatingGui:
    import os.path
    def __init__(self):
        
        self.master = Tk()
        self.fileN='ratings.csv'
        self.data = self.loadNames()
        self.master.title("App to update the rating")

        self.label = Label(self.master, text="Do you want to add another user or update the scores?")
        self.label.grid(row=0, column = 0, columnspan=4, sticky = 'ew', pady = 10, padx = 5)

        self.add_button = Button(self.master, text="Add names", command=self.addNameWin)
        #my_button.grid(row=3, column=1, sticky=tk.E + tk.W, pady=10)
        #self.add_button.pack(side=LEFT, fill=Y, expand=True, pady=10)
        self.add_button.grid(row=2, column = 0, sticky = 'ew', pady = 10, padx = 5)

        self.update_button = Button(self.master, text="Update", command=self.updateData)
        #self.update_button.pack(side=LEFT, fill=Y, expand=True, pady=10)
        self.update_button.grid(row=2, column = 2, sticky = 'ew', pady = 10, padx = 5)
        
        self.close_button = Button(self.master, text="Add a result", command=self.addResWin)
        # self.close_button.pack(side=LEFT, fill=Y, expand=True, pady=10)
        self.close_button.grid(row=2, column = 1, sticky = 'ew', pady = 10, padx = 5)

        
        self.close_button = Button(self.master, text="Dismiss", command=self.master.destroy)
        # self.close_button.pack(side=LEFT, fill=Y, expand=True, pady=10)
        self.close_button.grid(row=2, column = 3, sticky = 'ew', pady = 10, padx = 5)

    def loadNames(self):
        import os.path
        if os.path.isfile(self.fileN):
            self.data={}
            with open(self.fileN) as f:
                line = f.readline()
                if len(line)>0:
                    while line:
                        values = line.split(',')
                        self.data[(values[0],values[1])]=values[2]
                        line = f.readline()
                else:
                    self.data={}
        else:
            self.data={}
        return self.data
            
    def addNameWin(self):
        from tkinter import Toplevel, Button, Entry, Label
        self.top = Toplevel()
        self.top.title("Please add first and family name")
        
        self.label = Label(self.top, text="First name")
        self.label.grid(row=0, column = 0, columnspan=1, sticky = 'ew', pady = 10, padx = 5)
        
        self.label = Label(self.top, text="Family name")
        self.label.grid(row=0, column = 1, columnspan=1, sticky = 'ew', pady = 10, padx = 5)
        
        self.label = Label(self.top, text="Initial rating")
        self.label.grid(row=0, column = 2, columnspan=1, sticky = 'ew', pady = 10, padx = 5)
        
        self.first_entry = Entry(self.top, text = 'First Name')
        self.first_entry.grid(row=1, column = 0, columnspan=1, sticky = 'ew', pady = 2, padx = 5)
        
        self.family_entry = Entry(self.top, text = 'Family Name')
        self.family_entry.grid(row=1, column = 1, columnspan=1, sticky = 'ew', pady = 2, padx = 5)
        
        self.rating_entry = Entry(self.top, text = 'Rating')
        self.rating_entry.grid(row=1, column = 2, columnspan=1, sticky = 'ew', pady = 2, padx = 5)
        self.rating_entry.insert(0,'1000')
        
        self.close_button = Button(self.top, text="Dismiss", command=self.top.destroy)
        self.close_button.grid(row=3, column = 0, columnspan=1, sticky = 'ew', pady = 10, padx = 5)
        
        self.ok_button = Button(self.top, text="OK", command=self.addName)
        self.ok_button.grid(row=3, column = 2, columnspan=1, sticky = 'ew', pady = 10, padx = 5)
        
    def addResWin(self):
        from tkinter import Toplevel, Button, Entry, Label
        names=[' '.join(key) for key in self.data.keys()]
        self.topList = Toplevel()
        self.topList.title("Please choose the players and the result")
        
        self.label = Label(self.topList, text="Choose player 1")
        self.label.grid(row=0, column = 0, columnspan=1, sticky = 'ew', pady = 10, padx = 5)
        
        self.label = Label(self.topList, text="Choose player 2")
        self.label.grid(row=0, column = 1, columnspan=1, sticky = 'ew', pady = 10, padx = 5)
        
        self.label = Label(self.topList, text="Who won?")
        self.label.grid(row=0, column = 2, columnspan=1, sticky = 'ew', pady = 10, padx = 5)
        
        self.first_combo = ttk.Combobox(self.topList,values=names)
        self.first_combo.grid(row=1, column = 0, columnspan=1, sticky = 'ew', pady = 2, padx = 5)
        
        
        self.second_combo = ttk.Combobox(self.topList,values=names)
        self.second_combo.grid(row=1, column = 1, columnspan=1, sticky = 'ew', pady = 2, padx = 5)
        
        
        self.result_combo = ttk.Combobox(self.topList,values=['1','2'])
        self.result_combo.grid(row=1, column = 2, columnspan=1, sticky = 'ew', pady = 2, padx = 5)
  
        
        self.close_button = Button(self.topList, text="Dismiss", command=self.topList.destroy)
        self.close_button.grid(row=3, column = 0, columnspan=1, sticky = 'ew', pady = 10, padx = 5)
        
        self.ok_button = Button(self.topList, text="OK", command=self.addResult)
        self.ok_button.grid(row=3, column = 2, columnspan=1, sticky = 'ew', pady = 10, padx = 5)
    
    def addResult(self):
        ind_first = self.first_combo.get().split()
        ind_second = self.second_combo.get().split()
        ind_res=int(self.result_combo.get()) # result of the match
        print(ind_first)
        keys=list(self.data.keys())
        print(keys)
        print(self.data)
        res1=self.data[(ind_first[0],ind_first[1])] # current rating of the first person
        res2=self.data[(ind_second[0],ind_second[1])] # current rating of the second person
        new_res1,new_res2=self.EloRating(res1,res2,ind_res)
        self.data[(ind_first[0],ind_first[1])]=str(new_res1)
        self.data[(ind_second[0],ind_second[1])]=str(new_res2)
        self.topList.destroy()

    def Probability(rating1, rating2): 
        import math
        return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (rating1 - rating2) / 400)) 

    def EloRating(Ra, Rb, d):
	K=32 
        # To calculate the Winning 
        # Probability of Player B 
     	Pb = self.Probability(Ra, Rb) 
  
    	# To calculate the Winning 
    	# Probability of Player A 
    	Pa = self.Probability(Rb, Ra) 
  
    	# Case -1 When Player A wins 
    	# Updating the Elo Ratings 
    	if (d == 1) : 
            Ra = Ra + K * (1 - Pa) 
            Rb = Rb + K * (0 - Pb) 
      
  
      	# Case -2 When Player B wins 
    	# Updating the Elo Ratings 
    	else : 
            Ra = Ra + K * (0 - Pa) 
            Rb = Rb + K * (1 - Pb) 
       	return(round(Ra, 6),round(Rb, 6)) 
        
    def addName(self):
        try:
            name=(self.first_entry.get().strip().capitalize(), self.family_entry.get().strip().capitalize())
            try:
                isinstance(int(self.rating_entry.get()), int)
                self.data[name]=str(self.rating_entry.get())
                print(self.data)
            except:
                messagebox.showwarning("Warning","The rating must be a number")
            
            self.first_entry.delete(0,'end')
            self.family_entry.delete(0,'end')
            self.rating_entry.delete(0,'end')
            self.top.destroy()
        except:
            print('Bad name')
            
    def updateData(self):
        print(self.data)
        with open(self.fileN,'w') as f:
            for keys,value in self.data.items():
                f.write(','.join([keys[0]]+[keys[1]]+[value]+['\n']))
        self.master.destroy()
            


if __name__ == "__main__":
    main()

updatedrating_1= currentrating_1+32*(score_1-(10^(currentrating_1/400)/((currentrating_1/400)+10^(currentrating_2/400))