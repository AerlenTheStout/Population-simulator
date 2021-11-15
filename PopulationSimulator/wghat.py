import tkinter as tk

def change_label(*args):
    label.config(text='') # clear label
    label.config(text='T' + var.get()) # set new label text

root = tk.Tk()

var = tk.StringVar() # make the StringVar()

label = tk.Label(root)
entry = tk.Entry(root, textvariable=var) # set the textvariable to var

var.trace('w', change_label) # trace var to monitor for changes, calling function on change

label.pack()
entry.pack()

root.mainloop()