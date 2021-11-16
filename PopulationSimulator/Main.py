import tkinter as tk

def changeWaterLabel(*args):
    ST.WaterLabel.config(text='') # clear label
    ST.WaterLabel.config(text= "Water = " + ST.numOfWaterEntry.get()) # set new label text

def changeFoodLabel(*args):
    ST.FoodLabel.config(text='') # clear label
    ST.FoodLabel.config(text= "Food = " + ST.numOfFoodEntry.get()) # set new label text

def changeShelterLabel(*args):
    ST.ShelterLabel.config(text='') # clear label
    ST.ShelterLabel.config(text= "Shelter = " + ST.numOfShelterEntry.get()) # set new label text

def changeYearLabel(*args):
    ST.yearLabel.config(text='') # clear label
    ST.yearLabel.config(text="Year " + str(year)) # set new label text

def ST():

    #Intalize Tkinter
    ST.root = tk.Tk()
    ST.root.title('Ecosystem Population Simulator')

    #make traceable variables
    ST.WaterVar = tk.StringVar()
    ST.FoodVar = tk.StringVar()
    ST.ShelterVar = tk.StringVar()

    #make entry boxes
    ST.numOfWaterEntry = tk.Entry(ST.root, width=10,textvariable=ST.WaterVar)
    ST.numOfFoodEntry = tk.Entry(ST.root, width=10,textvariable=ST.FoodVar)
    ST.numOfShelterEntry = tk.Entry(ST.root, width=10,textvariable=ST.ShelterVar)

    #make changeable labels
    ST.WaterLabel = tk.Label(ST.root,text="Water = 0")
    ST.FoodLabel = tk.Label(ST.root,text="Food = 0")
    ST.ShelterLabel = tk.Label(ST.root,text="Shelter = 0")

    #makes year counter label and variable
    ST.yearLabel = tk.Label(ST.root, text="")
    global year; year = 0

    #change label
    ST.WaterVar.trace('w', changeWaterLabel)
    ST.FoodVar.trace('w', changeFoodLabel)
    ST.ShelterVar.trace('w', changeShelterLabel)
    
    #place on screen
    ST.numOfWaterEntry.grid(row=3, column=1)
    ST.numOfFoodEntry.grid(row=3,column=2)
    ST.numOfShelterEntry.grid(row=3,column=3)
    ST.WaterLabel.grid(row=2,column=1)
    ST.FoodLabel.grid(row=2,column=2)
    ST.ShelterLabel.grid(row=2,column=3)
    ST.yearLabel.grid(row=1,column=2)
    ActivateButton = tk.Button(ST.root, padx=10, pady=10,text='Advance', command=activate)
    
    ActivateButton.grid(row=4,column=2)

    ST.root.mainloop()

def activate():
    global year; year += 1
    changeYearLabel()
    
ST()