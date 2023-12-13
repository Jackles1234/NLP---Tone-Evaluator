from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from classify import classifier
root = Tk()
root.geometry("1000x800")
root.title(" Email Tone Evalutator ")
 
def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    Primary, Secondary = classifier(INPUT)
    Output1.insert(END, Primary)
    Output2.insert(END, Secondary)
    
       
     
l = Label(text = "Enter your drafted Email")
inputtxt = Text(root, height = 17,
                width = 65,
                bg = "light yellow")

l2 = Label(text = "Primary Tone Identified")
Output1 = Text(root, height = 7,
              width = 45,
              bg = "light cyan")
l3 = Label(text = "Other Prominent Words")
Output2 = Text(root, height = 7,
              width = 45,
              bg = "light green")
 
Display = Button(root,
                 text ="Show",
                 command = lambda:Take_input())
 
l.pack()
inputtxt.pack()
Display.pack()
l2.pack()
Output1.pack()
l3.pack()
Output2.pack()
 
mainloop()