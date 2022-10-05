
from distutils import command
from email.utils import decode_params
from msilib.schema import RadioButton
from tkinter import * 
import tkinter as tk
from tkinter import ttk
from turtle import ScrolledCanvas
from  test2 import *

class Case(tk.Frame):
    nbremptycase=0
    filledlist=[]
    
    def __init__(self, parent,j):
        tk.Frame.__init__(self, parent,bg="#ec0062",borderwidth=1)
        vcmd = (self.register(self.onValidate),'%S','%P')
        self.label=tk.Label(self,text=f"Index : {j+1}",bg="#ec0062")
        self.entry = tk.Entry(self,justify=CENTER, width=10,
        validate="key", validatecommand=vcmd)
        self.label.pack()
        self.entry.pack()
        self.id=j
        self.grid(row=(j//10)+10,column=j % 10,padx=5,pady=5)
        self.point=False
    def onValidate(self,S,P):
        try: 
            float(S)
            if(len(P)>0):
                if(Case.filledlist[self.id]==0):
                      Case.nbremptycase-=1
                self.label.config(bg="#28B463")
                Case.filledlist[self.id]=1
                if(Case.nbremptycase==0):
                    trie.configure(state='active')
                    
            else :
                Case.filledlist[self.id]=0
                Case.nbremptycase+=1
                trie.configure(state='disabled')
                self.label.config(bg="#ec0062")    
            return True
        except ValueError:
            limitexceeded.configure(text="Only number")
            return False 



window = tk.Tk()
    #variables
window.geometry('900x600+220+40')
radioValue = tk.IntVar() 
typetrie=tk.StringVar()
value=tk.StringVar()
trietypes=["insertion","bulle"]
data=tk.Frame(master=window)
result=tk.Frame(master=window)
cases=[]
valueslist=[]
#functions
def addemptycase(n):
    global cases
    try: 
        n=int(n)
    except ValueError:
        n=0
    for widget in result.winfo_children():
          widget.destroy() 
    cases.append(Case(data,n))
    nbrcase.configure(state='normal')
    nbrcase.delete(0,END)
    nbrcase.insert(0,n+1)
    nbrcase.configure(state='disabled')
    trie.configure(state='disabled')
    creat.configure(state='disabled')
    clear.configure(state='active')
    Case.filledlist.append(0)
    Case.nbremptycase+=1



def gettype():
    global nbrcase2
    nbrcase2=tk.Label(text=typetrie.get()+"  "+str(radioValue.get())).pack(padx=5,pady=5)

def fillcase():
      pass

def clearlist():
    global valueslist
    global cases
    cases=[]
    valueslist=[]
    for widget in data.winfo_children():
          widget.destroy()
    for widget in result.winfo_children():
          widget.destroy() 
    trie.configure(state='disabled')
    nbrcase.configure(state='normal')
    clear.configure(state='disabled')
    creat.configure(state='active')
    addcase.configure(state='disabled')

def creatlist(n):
    global cases
    global valueslist
    valueslist=[]
    try:
        if(int(n)<0):
            print(2/0)
        n=int(n)
        Case.nbremptycase=n
        Case.filledlist=[0]*n
        for widget in result.winfo_children():
            widget.destroy()
        tk.Label(master=data,text="Fill The cases").grid(column=0,row=0)
        for j in range(n):
            cases.append(Case(data,j)) 
        nbrcase.configure(state='disabled')
        creat.configure(state='disabled')
        clear.configure(state='active')
        addcase.configure(state='active')
    except ValueError:
        errormsg.configure(text="Enter a positive number not null please")
    except ZeroDivisionError:
        errormsg.configure(text="Enter a positive number not null please")

def trielist():
    global cases
    global valueslist
    valueslist=[]
    i=0
    for  case in cases:
        valueslist.append(float(case.entry.get()))
    if typetrie.get()=="bulle":
        bulle(valueslist)
    elif typetrie.get()=="insertion":
        selection(valueslist)

    tk.Label(master=result,text="The sorted list :").grid(column=0,row=0)
    for case in cases:
      tried = tk.Frame(
            master=result,
            relief=tk.RAISED,
            borderwidth=1,
            bg="#ffc30f"
      )
      tried.grid(row=(i//10)+10,column=i % 10,padx=5,pady=5)
      index=tk.Label(master=tried,text=f"Index : {i+1}",bg="#ffc30f")
      value=tk.Label(master=tried,bg="white",width=10)
      if radioValue.get()==0:
          value.configure(text=f"{valueslist[i]}")
      else:
          value.configure(text=f"{valueslist[-i-1]}")    
      i+=1
      index.pack()
      value.pack()   
    


#widgets created
typeoftrie=tk.Label(text="Enter the trie sens") 
asc = tk.Radiobutton(window, text='ASC',variable=radioValue,value=0) 
desc = tk.Radiobutton(window, text='DESC',variable=radioValue, value=1)

typetext=tk.Label(text="Pick an trie's type") 
typelist = ttk.Combobox( values = trietypes,textvariable=typetrie)
typelist.set("socktrie")

nbrtext=tk.Label(text="Enter the list's length")
nbrcase=tk.Entry()      
creat=tk.Button(window,text="Creat",command= lambda :creatlist(nbrcase.get()))
clear=tk.Button(window,text="Clear",command= lambda :clearlist(),state=DISABLED)
addcase=tk.Button(window,text="Add case",command=lambda : addemptycase(nbrcase.get()),state=DISABLED)
trie=tk.Button(window,text="Sort",command= lambda :trielist(),state=DISABLED)
errormsg=tk.Label(text="")
limitexceeded=tk.Label(text="")







#emplacement of Widgets
typeoftrie.pack()
asc.pack()
desc.pack()
typetext.pack(padx=5,pady=5)
typelist.pack(padx = 5, pady = 5)
nbrtext.pack(padx=5,pady=5)
nbrcase.pack(padx=5, pady=5)
errormsg.pack(padx=5,pady=5)
creat.pack(padx=5, pady=5)
clear.pack(padx=5, pady=5)
addcase.pack(padx=5,pady=5)
trie.pack(padx=5,pady=5)
limitexceeded.pack(padx=5,pady=5)
data.pack()
result.pack()
window.title("HT. Salmen Sorting Program")
window.resizable(False,False)
window.mainloop()