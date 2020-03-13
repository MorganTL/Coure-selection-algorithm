# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 20:03:03 2020

@author: Morgan
"""

import tkinter as tk
from course_selection_redux import basicsorting
from course_selection_redux import dayoffsorting

def inportfile():
    with open('input.txt', "r") as f:
        text = f.read()
    return text


def savefile():    
    user_input = text_input.get("1.0", tk.END)
    with open('input.txt', "w") as f:
        f.write(user_input)







window = tk.Tk()
window.title("Class selection algorithm")
#----------------
#Here is the frame and text input and output
frame1 = tk.Frame(master = window,width = 400, height = 50, bg = '#000000')

frame_input = tk.Frame(master = window,width = 340, height = 900, bg = '#000000')

frame_output = tk.Frame(master = window,width = 400, height = 900, bg = '#000000')

text_input = tk.Text(master = frame_input, font = ("calibri", 11), bg = '#9370DB', fg = "#f5f5f5",
                     highlightcolor='#1F1B24' ,highlightbackground='#121212', highlightthickness=10, bd =0)


label_ouput = tk.Label(master = frame_output, text = 'Waiting input', justify='left',
                       font = ("calibri", 11), bg = '#121212', fg = "#BB86FC" )

#-----------------
#function related to text input and output
def changetext(word):    
    label_ouput.config(text=str(word))              

def basic_mode():
    word = basicsorting('input.txt')
    changetext(word)

def day_off_mode():
    word = dayoffsorting('input.txt')   
    changetext(word)
    
def both_mode():
    word = basicsorting('input.txt') + dayoffsorting('input.txt')   
    changetext(word)
    
    
    
#---------------
#Below are all the buttons 
label_input = tk.Button(master = frame1, text = "Save", command = savefile,
                        bg = '#121212', fg = 'white',activebackground= "#6200EE", 
                      activeforeground ='white')
btn_basic = tk.Button(master = frame1, text = "Basic mode", command = basic_mode,
                      bg = '#121212', fg = 'white',activebackground= "#6200EE", 
                      activeforeground ='white')
btn_dayoff = tk.Button(master = frame1, text = "Dayoff priority mode", command = day_off_mode,
                       bg = '#121212', fg = 'white',activebackground= "#6200EE", 
                      activeforeground ='white')
# btn_both = tk.Button(master = frame1, text = "BOTH")







frame1.pack(fill = tk.X, side = tk.TOP)
frame_output.pack(fill = tk.BOTH, side = tk.RIGHT, expand=True)
frame_input.pack(fill = tk.BOTH, side = tk.TOP, expand=True)


label_input.place(x=145,y=20)
btn_basic.place(x=390,y=20)
btn_dayoff.place(x=490,y=20)
# btn_both.place(x=560,y=20)

text_input.place(x = 20, y=20,width = 300, height = 850)
label_ouput.place(x = 40, y=20,width = 320, height = 850)


text_input.insert("1.0", str(inportfile()))


window.mainloop()






























