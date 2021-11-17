import tkinter as tk
import random as rd

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
    for i in range(int(ST.AnimalVar.get())):
        Animals.append(rd.randint(1,3))
    print(Animals)

    #count needs
    Waterneed = Animals.count(1)
    print(Waterneed, "waterneed")
    FoodNeed = Animals.count(2)
    print(FoodNeed, "foodneed")
    ShelterNeed = Animals.count(3)
    print(ShelterNeed, "shelterneed")

    #get values from entry boxes
    numOfWater = int(ST.numOfWaterEntry.get())
    print(numOfWater,"Water")
    numOfFood = int(ST.numOfFoodEntry.get())
    print(numOfFood, "food")
    numOfShelter = int(ST.numOfShelterEntry.get())
    print(numOfShelter, "shelter")

    #find out difference between needs and animals needs
    WaterLeft = numOfWater - Waterneed
    print(WaterLeft, "WaterLeft")
    FoodLeft = numOfFood - FoodNeed
    print(FoodLeft, "FoodLeft")
    ShelterLeft =  numOfShelter - ShelterNeed
    print(ShelterLeft, "ShelterLeft")
    
    #change entry boxes to how many elements are left
    if WaterLeft < 0:
        WaterToRemove = 0
    else:
        WaterToRemove = WaterLeft
    if FoodLeft < 0:
        FoodToRemove = 0
    else:    
        FoodToRemove = FoodLeft
    if ShelterLeft < 0:
        ShelterToRemove = 0
    else:
        ShelterToRemove = ShelterLeft
    
    ST.WaterVar.set(WaterToRemove)
    ST.FoodVar.set(FoodToRemove)
    ST.ShelterVar.set(ShelterToRemove)

    #if there is enough water, food, and shelter, then remove animals from array
    if WaterLeft < 0:
        for i in range(abs(WaterLeft)):
            Animals.pop(0)
            print(Animals)
    if FoodLeft < 0:
        for i in range(abs(FoodLeft)):
            Animals.pop(0)
            print(Animals)
    if ShelterLeft < 0:
        for i in range(abs(ShelterLeft)):
            Animals.pop(0)
            print(Animals)
    #edit config of entry boxes
    ST.AnimalVar.set(len(Animals))



    #Add animals to array
    AnimalsToAdd = numOfWater - WaterLeft, numOfFood - FoodLeft, numOfShelter - ShelterLeft
    print(AnimalsToAdd, "AnimalsToAdd")
    
ST()

