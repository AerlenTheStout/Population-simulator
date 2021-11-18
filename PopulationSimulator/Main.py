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

def changeWaterCapVar(*args):
    ST.WaterCap.config(text='') # clear label
    ST.WaterCap.config(text= "Water Cap = " + ST.WaterCapEntry.get()) # set new label text

def changeFoodCapVar(*args):
    ST.FoodCap.config(text='') # clear label
    ST.FoodCap.config(text= "Food Cap = " + ST.WaterCapEntry.get()) # set new label text

def changeShelterCapVar(*args):
    ST.ShelterCap.config(text='') # clear label
    ST.ShelterCap.config(text= "Shelter Cap = " + ST.ShelterCapEntry.get()) # set new label text

def ST():

    #Intalize Tkinter
    ST.root = tk.Tk()
    ST.root.title('Ecosystem Population Simulator')

    #make traceable variables
    ST.WaterVar = tk.IntVar()
    ST.FoodVar = tk.IntVar()
    ST.ShelterVar = tk.IntVar()

    ST.AnimalVar = tk.IntVar()

    ST.WaterCapVar = tk.IntVar()
    ST.FoodCapVar = tk.IntVar()
    ST.ShelterCapVar = tk.IntVar()

    #make entry boxes
    ST.numOfWaterEntry = tk.Entry(ST.root, width=10,textvariable=ST.WaterVar)
    ST.numOfFoodEntry = tk.Entry(ST.root, width=10,textvariable=ST.FoodVar)
    ST.numOfShelterEntry = tk.Entry(ST.root, width=10,textvariable=ST.ShelterVar)

    #make element cap entry boxes
    ST.WaterCapEntry = tk.Entry(ST.root, width=10,textvariable=ST.WaterCapVar)
    ST.FoodCapEntry = tk.Entry(ST.root, width=10,textvariable=ST.FoodCapVar)
    ST.ShelterCapEntry = tk.Entry(ST.root, width=10,textvariable=ST.ShelterCapVar)

    #make animal entry boxes
    ST.numOfAnimalsEntry = tk.Entry(ST.root, width=10,textvariable=ST.AnimalVar)

    #make changeable labels
    ST.WaterLabel = tk.Label(ST.root,text="Water = 0")
    ST.FoodLabel = tk.Label(ST.root,text="Food = 0")
    ST.ShelterLabel = tk.Label(ST.root,text="Shelter = 0")
    
    #make element caps labels
    ST.WaterCap = tk.Label(ST.root,text="Water Cap = 0")
    ST.FoodCap = tk.Label(ST.root,text="Food Cap = 0")
    ST.ShelterCap = tk.Label(ST.root,text="Shelter Cap = 0")

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

    ST.WaterCapVar.trace('w', changeWaterCapVar)
    ST.FoodCapVar.trace('w', changeFoodCapVar)
    ST.ShelterCapVar.trace('w', changeShelterCapVar)
    


    #place on screen
    ST.YearLabel.grid(row=1,column=2)
    
    ST.WaterCap.grid(row=2,column=1)
    ST.FoodCap.grid(row=2,column=2)
    ST.ShelterCap.grid(row=2,column=3)

    ST.WaterCapEntry.grid(row=3, column=1)
    ST.FoodCapEntry.grid(row=3,column=2)
    ST.ShelterCapEntry.grid(row=3,column=3)

    ST.WaterLabel.grid(row=4,column=1)
    ST.FoodLabel.grid(row=4,column=2)
    ST.ShelterLabel.grid(row=4,column=3)

    ST.numOfWaterEntry.grid(row=5, column=1)
    ST.numOfFoodEntry.grid(row=5,column=2)
    ST.numOfShelterEntry.grid(row=5,column=3)

    ST.AnimalLabel.grid(row=6,column=2)

    ST.numOfAnimalsEntry.grid(row=7, column=2)

    #activate button
    ActivateButton = tk.Button(ST.root, padx=10, pady=10,text='Advance', command=activate)
    ActivateButton.grid(row=8,column=2)

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
    print(len(Animals))

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

    #add resources
    for i in range(len(Animals)):
        RandNum = rd.randint(1,3)
        if RandNum == 1:
            ST.WaterVar.set(ST.WaterVar.get() + 1)
        if RandNum == 2:
            ST.FoodVar.set(ST.FoodVar.get() + 1)
        if RandNum == 3:
            ST.ShelterVar.set(ST.ShelterVar.get() + 1)
    print(ST.WaterVar.get(), "newWater")
    print(ST.FoodVar.get(), "newFood")
    print(ST.ShelterVar.get(), "Shelter")
    
    #limit elements to cap
    if ST.FoodVar.get() > ST.FoodCapVar.get():
        ST.FoodVar.set(ST.FoodCapVar.get())
    if ST.WaterVar.get() > ST.WaterCapVar.get():
        ST.WaterVar.set(ST.WaterCapVar.get())
    if ST.ShelterVar.get() > ST.ShelterCapVar.get():
        ST.ShelterVar.set(ST.ShelterCapVar.get())

    #if there is not enough water, food, and shelter, then remove animals from array
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
    #ST.AnimalVar.set(len(Animals))
    

    #Add animals to array
    
    if WaterToRemove <= 0:
        AnimalsToAdd = numOfWater
    else:
        AnimalsToAdd = numOfWater - WaterToRemove
    if FoodToRemove <= 0:
        AnimalsToAdd += numOfFood
    else:
        AnimalsToAdd += numOfFood - FoodToRemove
    if ShelterToRemove <= 0:
        AnimalsToAdd += numOfShelter
    else:
        AnimalsToAdd += numOfShelter - ShelterToRemove
    print(AnimalsToAdd, "AnimalsToAdd")
    ST.AnimalVar.set(AnimalsToAdd + len(Animals))
    print(AnimalsToAdd + len(Animals), "Animals")
    
    
ST()

