# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the window
win.geometry("700x350")

# Define a function on mouse button clicked
def on_click(event):
   label["text"]="Hello, There!"

def on_release(event):
   label["text"]="Button Released!"

# Crate a Label widget
label=Label(win, text="Click anywhere..", font=('Calibri 18 bold'))
label.pack(pady=60)

win.bind("<ButtonPress-1>", on_click)
win.bind("<ButtonRelease-1>", on_release)

win.mainloop()