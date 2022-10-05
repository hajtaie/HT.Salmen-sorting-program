# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create a canvas widget
canvas=Canvas(win, width=500, height=300,scrollregion=True)
canvas.pack()

# Add a line in canvas widget
canvas.create_line(100,200,200,35, fill="green", width=5)
for i in range(40):
    bot=Button(master=canvas,text="hello").pack()
canvas.create_line(100,200,200,35, fill="green", width=5)

win.mainloop()

"""typeoftrie.place(bordermode=INSIDE,height=20,width=200,x=20,y=10)
asc.place(bordermode=INSIDE,height=10,width=200,x=20,y=40)
desc.place(bordermode=INSIDE,height=10,width=200,x=20,y=60)
typetext.place(bordermode=INSIDE,height=20,width=200,x=650,y=10)
typelist.place(bordermode=INSIDE,height=20,width=100,x=700,y=40)"""