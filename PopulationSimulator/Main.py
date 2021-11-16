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
    ST.YearLabel.config(text='') # clear label
    ST.YearLabel.config(text="Year " + str(year)) # set new label text

def changeAnimalLabel(*args):
    ST.AnimalLabel.config(text='') # clear label
    ST.AnimalLabel.config(text= "Animals =  " + ST.numOfAnimalsEntry.get()) # set new label text

def ST():

    #Intalize Tkinter
    ST.root = tk.Tk()
    ST.root.title('Ecosystem Population Simulator')

    #make traceable variables
    ST.WaterVar = tk.StringVar()
    ST.FoodVar = tk.StringVar()
    ST.ShelterVar = tk.StringVar()
    ST.AnimalVar = tk.StringVar()
    
    #make entry boxes
    ST.numOfWaterEntry = tk.Entry(ST.root, width=10,textvariable=ST.WaterVar)
    ST.numOfFoodEntry = tk.Entry(ST.root, width=10,textvariable=ST.FoodVar)
    ST.numOfShelterEntry = tk.Entry(ST.root, width=10,textvariable=ST.ShelterVar)

    #make animal entry boxes
    ST.numOfAnimalsEntry = tk.Entry(ST.root, width=10,textvariable=ST.AnimalVar)

    #make changeable labels
    ST.WaterLabel = tk.Label(ST.root,text="Water = 0")
    ST.FoodLabel = tk.Label(ST.root,text="Food = 0")
    ST.ShelterLabel = tk.Label(ST.root,text="Shelter = 0")

    #makes year counter label and variable
    ST.YearLabel = tk.Label(ST.root, text="Year 0")
    global year; year = 0

    #make animal label
    ST.AnimalLabel = tk.Label(ST.root, text="Animals = ")

    #change label
    ST.WaterVar.trace('w', changeWaterLabel)
    ST.FoodVar.trace('w', changeFoodLabel)
    ST.ShelterVar.trace('w', changeShelterLabel)
    ST.AnimalVar.trace('w', changeAnimalLabel)

    #place on screen
    ST.numOfWaterEntry.grid(row=3, column=1)
    ST.numOfFoodEntry.grid(row=3,column=2)
    ST.numOfShelterEntry.grid(row=3,column=3)
    ST.numOfAnimalsEntry.grid(row=5, column=2)
    ST.WaterLabel.grid(row=2,column=1)
    ST.FoodLabel.grid(row=2,column=2)
    ST.ShelterLabel.grid(row=2,column=3)
    ST.YearLabel.grid(row=1,column=2)
    ST.AnimalLabel.grid(row=4,column=2)
    
    ActivateButton = tk.Button(ST.root, padx=10, pady=10,text='Advance', command=activate)
    
    ActivateButton.grid(row=6,column=2)

    ST.root.mainloop()

def activate():
    
    #disable entry boxes
    ST.numOfWaterEntry.config(state='disabled')
    ST.numOfFoodEntry.config(state='disabled')
    ST.numOfShelterEntry.config(state='disabled')
    ST.numOfAnimalsEntry.config(state='disabled')

    #change year label
    global year; year += 1
    changeYearLabel()

    #make array for anmimals
    global Animals; Animals = []





    #get values from entry boxes
    numOfWater = int(ST.numOfWaterEntry.get())
    numOfFood = int(ST.numOfFoodEntry.get())
    numOfShelter = int(ST.numOfShelterEntry.get())

ST()

