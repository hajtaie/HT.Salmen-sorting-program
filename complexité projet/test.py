from cProfile import label
from distutils import command
from msilib.schema import RadioButton
from tkinter import * 
import tkinter as tk
from tkinter import ttk
from turtle import ScrolledCanvas

from pip import main

class Case(tk.Frame):
      def __int__(self,parent,i):
         tk.Frame.__init__(self,parent,relief=tk.RAISED,
            borderwidth=1,
            bg="#ec0062")
         vcmd = (self.register(self,self.check),'%S')
         self.label=tk.Label(self,text=f"Index : {i+1}",bg="#ec0062")
         self.entry=tk.Entry(self,width=10,justify=CENTER,validate='Key',validatecommand=vcmd)
         self.label.pack()
         self.entry.pack()
      
      def check(S):
          if not S == S.lower():
            return True
          else:
             self.bell()
             return False
          

window = tk.Tk() 

# creating and placing scrollbar


#variables
window.geometry('150x100')
radioValue = tk.IntVar() 
typetrie=tk.StringVar()
value=tk.StringVar()
trietypes=["Insertion","A bulle","Selection","Shell"]
data=tk.Frame(master=window)
result=tk.Frame(master=window)
#functions

def deletelastcase(n):
    for widget in result.winfo_children():
          widget.destroy() 
    l.pop().destroy()
    nbrcase.configure(state='normal')
    nbrcase.delete(0,END)
    nbrcase.insert(0,n-1)
    nbrcase.configure(state='disabled')
    Case.filledlist.pop()
    if Case.nbremptycase==0 :
        trie.configure(state='active')
    if n-1==0:
        deletecase.configure(state='disabled')    
        trie.configure(state='disabled')    
        clear.configure(state='disabled')    
        creat.configure(state='active')
        nbrcase.configure(state='normal')   
    print(Case.filledlist)   
    print(Case.nbremptycase)


def gettype():
    global nbrcase2
    nbrcase2=tk.Label(text=typetrie.get()+"  "+str(radioValue.get())).pack(padx=5,pady=5)

def fillcase():
      pass

def clearlist():
    for widget in data.winfo_children():
          widget.destroy()
    for widget in result.winfo_children():
          widget.destroy() 
    trie.configure(state='disabled')
    nbrcase.configure(state='normal')
    clear.configure(state='disabled')
    creat.configure(state='active')   

def creatlist(n): 
    for widget in result.winfo_children():
          widget.destroy()
    for i in range(n):
         Case(data,i).grid(row=(i//10)+10,column=i % 10,padx=5,pady=5)
    trie.configure(state='active')
    nbrcase.configure(state='disabled')
    creat.configure(state='disabled')
    clear.configure(state='active')


def trielist(n):
    tk.Label(master=result,text="The tried list :").grid(column=0,row=0)
    for i in range(n):
      tried = tk.Frame(
            master=result,
            relief=tk.RAISED,
            borderwidth=1,
            bg="#ffc30f"
      )
      tried.grid(row=(i//10)+10,column=i % 10,padx=5,pady=5)
      label=tk.Label(master=tried,text=f"Index : {i+1}",bg="#ffc30f")
      entry = tk.Entry(master=tried,width=10)
      label.pack()
      entry.pack()


#widgets created
typeoftrie=tk.Label(text="Enter the trie sens") 
asc = tk.Radiobutton(window, text='ASC',variable=radioValue,value=0) 
desc = tk.Radiobutton(window, text='DESC',variable=radioValue, value=1)

typetext=tk.Label(text="Pick an trie's type") 
typelist = ttk.Combobox( values = trietypes,textvariable=typetrie)
typelist.set("socktrie")

nbrtext=tk.Label(text="Enter the list's length")
nbrcase=tk.Entry()      
creat=tk.Button(window,text="Creat",command= lambda :creatlist(int(nbrcase.get())))
clear=tk.Button(window,text="Clear",command= lambda :clearlist(),state=DISABLED)
#trie=tk.Button(window,text="Trie",command= lambda :trielist(int(nbrcase.get())))
trie=tk.Button(window,text="Trie",command= lambda :trielist(int(nbrcase.get())),state=DISABLED)
deletecase=tk.Button(window,text="Delete case",command=lambda : deletelastcase(int(nbrcase.get())),state=DISABLED)


#emplacement of Widgets
typeoftrie.pack()
asc.pack()
desc.pack()
typetext.pack(padx=5,pady=5)
typelist.pack(padx = 5, pady = 5)
nbrtext.pack(padx=5,pady=5)
nbrcase.pack(padx=5, pady=5)
creat.pack(padx=5, pady=5)
clear.pack(padx=5, pady=5)
deletecase.pack(padx=5,pady=5)
trie.pack(padx=5,pady=5)
data.pack()
result.pack()
window.minsize(760,500)

window.mainloop()