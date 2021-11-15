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

def ST():

    #Intalize Tkinter
    root = tk.Tk()
    root.title('Ecosystem Population Simulator')

    #make traceable variables
    ST.WaterVar = tk.StringVar()
    ST.FoodVar = tk.StringVar()
    ST.ShelterVar = tk.StringVar()

    #make entry boxes
    ST.numOfWaterEntry = tk.Entry(root, width=10,textvariable=ST.WaterVar)
    ST.numOfFoodEntry = tk.Entry(root, width=10,textvariable=ST.FoodVar)
    ST.numOfShelterEntry = tk.Entry(root, width=10,textvariable=ST.ShelterVar)

    #make changeable labels
    ST.WaterLabel = tk.Label(root,text="Water = 0")
    ST.FoodLabel = tk.Label(root,text="Food = 0")
    ST.ShelterLabel = tk.Label(root,text="Shelter = 0")

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

    root.mainloop()

ST()