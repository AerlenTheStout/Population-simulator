import tkinter as tk

def changeWaterLabel(*args):
    WaterLabel.config(text='') # clear label
    WaterLabel.config(text= numOfWaterEntry.get()) # set new label text

root = tk.Tk()
root.title('Ecosystem Population Simulator')

WaterVar = tk.StringVar()
WaterLabel = tk.Label(root)

numOfWaterEntry = tk.Entry(root, width=10,textvariable=WaterVar)

WaterVar.trace('w', changeWaterLabel)

numOfWaterEntry.grid(row=3, column=1)
WaterLabel.grid(row=2,column=1)

root.mainloop()