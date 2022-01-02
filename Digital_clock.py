#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter.ttk import *

from time import strftime

#cretating ui for clock

root = Tk()
root.title("CLOCK")

#defining function for time
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

#label to store clock
label = Label(root, font=("ds-digital", 80), background = "black", foreground = "cyan")
#packing label

label.pack(anchor = 'center')

#calling time function
time()
mainloop()

