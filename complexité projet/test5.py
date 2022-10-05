"""from tkinter import Tk, Label
root=Tk()
def key_pressed(event):
 w=Label(root,text="Key Pressed:"+event.char)
 w.place(x=70,y=90)
root.bind("<Key>",key_pressed)
root.mainloop()"""
#Import the tkinter library
from tkinter import *

#Create an instance of tkinter frame
win = Tk()

#Set the geometry
win.geometry("650x250")

def handler(e):
   label= Label(win, text= "You Pressed Enter")
   label.pack()

#Create a Label
Label(win, text= "Press Enter on the Keyboard", font= ('Helvetica bold', 14)).pack(pady=20)
Entry(win).pack()
#Bind the Enter Key to Call an event
win.bind('<Return>',handler)

win.mainloop()