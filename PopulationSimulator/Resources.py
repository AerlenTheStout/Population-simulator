import math
import random
import tkinter as tk




def Resources():
    
    numOfWater = int(numOfWaterEntry.get())
    numOfFood = int(numOfFoodEntry.get())
    numOfShelter = int(numOfShelterEntry.get())
    
    resources = {
        "Water": numOfWater,
        "Food": numOfFood,
        "Shelter": numOfShelter,
    }
