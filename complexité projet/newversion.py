from cProfile import label
from cgitb import text
from cmath import e
from distutils import command
from doctest import master
from email.utils import decode_params
from msilib.schema import RadioButton
from pickle import READONLY_BUFFER
from tkinter import * 
import tkinter as tk
from tkinter import ttk
from turtle import ScrolledCanvas, delay, st
import turtle
from venv import create

from numpy import delete
from  test2 import *
import winsound
from tkinter.tix import *
from tkinter.tix import *

class Case(tk.Frame):
    nbremptycase=0
    filledlist=[]
    def __init__(self, parent,j):
        tk.Frame.__init__(self, parent,bg="#ec0062",borderwidth=1)
        vcmd = (self.register(self.onValidate),'%P','%s')
        self.option=tk.Frame(self,bg="#ec0062")
        self.deleten=tk.Button(self.option,width=24,height=18,image=deletenumberimage,
        command=lambda : self.removenum(),cursor="hand2")
        self.deleteb=tk.Button(self.option,width=24,height=18,image=deleteboximage,
        command=lambda : self.delete(),cursor="hand2")
        self.label=tk.Label(self,text=f"Index : {j//2+1}",bg="#ec0062")
        self.entry = tk.Entry(self,justify=CENTER, width=9,
        validate="key", validatecommand=vcmd,font = ('calibre',10,'bold'))
        self.deleten.grid(column=0,row=0,padx=2)
        self.deleteb.grid(column=1,row=0,padx=0)
        self.label.pack()
        self.entry.pack()
        self.id=j//2
        self.grid(row=(j//20),column=j % 20,padx=5,pady=12)
        self.point=False
        self.bind("<Enter>",self.displayoption)
        self.bind("<Leave>",self.hideoption)
        self.deleteb.bind("<Enter>",Case.displaydbdesg)
        self.deleteb.bind("<Leave>",Case.hidedesg)
        self.deleten.bind("<Enter>",Case.displaydndesg)
        self.deleten.bind("<Leave>",Case.hidedesg)
        self.entry.bind("<Button-1>",Case.disaddesg)  
    
    def disaddesg(self):
        buttondes.config(text="Add left box (ctrl+l) / Add right box (ctrl+r)")

    def displaydbdesg(self):
        buttondes.config(text="Delete the box (ctrl+d)")
    
    def displaydndesg(self):
        buttondes.config(text="Remove the number (ctrl+e)")

    def hidedesg(self):
        buttondes.config(text="Add left box (ctrl+l) / Add right box (ctrl+r)")  

    def removenum(self):
        Case.filledlist[self.id]=0
        Case.nbremptycase+=1
        self.entry.delete(0,END)
        for box in result.winfo_children():
            box.destroy()
        restxt.pack_forget()
        trie.config(state=DISABLED,cursor="arrow")
    
    """def expand(self):
        global size
        size+=1"""

    def displayoption(self,e):
        """global size
        count=0
        while count <18:
            self.after(5000,self.expand)
            self.option.pack()
            count+=1"""
        self.grid_forget()
        self.option.pack()
        self.grid(row=self.id*2//20,column=(self.id*2) % 20+1,padx=5,pady=0)

    def hideoption(self,e):
        self.grid_forget()
        self.option.pack_forget()
        self.grid(row=self.id*2//20,column=(self.id*2) % 20+1,padx=5,pady=12)
        

    def delete(self):
        values=[]
        global cases
        global newcases
        if Case.filledlist[self.id]==0:
           Case.nbremptycase-=1
        del Case.filledlist[self.id]   
        self.destroy()
        for widget in result.winfo_children():
           widget.destroy() 
        n=nbrcase.get()
        if int(n)-1 !=0:
            nbrcase.configure(state='normal')
            nbrcase.delete(0,END)
            nbrcase.insert(0,str(int(n)-1))
            nbrcase.config(state='disabled')
            cases=[]
            newcases=[]
            for box in data.winfo_children():
                if type(box)==Case:
                    values.append(box.entry.get())
                box.destroy()
            for i in range(len(values)*2):
                if i % 2 == 0:
                    newcases.append(Newcase(data,i))
                else:    
                    cases.append(Case(data,i))
                    cases[i//2].entry.insert(0,values[i//2])
                    if i//2==self.id-1:
                        cases[i//2].entry.focus_set()
                    elif self.id==0:
                        cases[0].entry.focus_set()
            
            newcases.append(Newcase(data,2*int(n)-2))              
            #trielist()    

        else:
            clearlist()    

    def checkstr(self,str):
        if len(str)==1:
            if str[0]=='-':
                return True
            else:
                try:
                    float(str)
                    return True
                except ValueError:
                    return False
        elif '.' in str and str[0]=='-':
            if str[1]=='.':
                return False
            else: 
                try:
                    float(str)
                    print(str)
                    return True
                except ValueError:
                    return False
        elif len(str)==0:
            print("is empty")
            return True              
        else:
            try:
                float(str)
                return True
            except ValueError:
                return False            


    def onValidate(self,P,s):
        if self.checkstr(P) :
            limitexceeded.config(text="")
            if len(P)==1 and P[0]=='-':
                self.label.config(bg="#ec0062")
                self.config(bg="#ec0062")
                if Case.filledlist[self.id]==1:
                    Case.filledlist[self.id]=0
                    Case.nbremptycase+=1
                    trie.configure(state='disabled',cursor='arrow')
                    print(P)
                return True
            elif len(P)==0 and Case.filledlist[self.id]==1:
                print("s= ",s)
                Case.filledlist[self.id]=0
                Case.nbremptycase+=1
                self.label.config(bg="#ec0062")
                self.option.config(bg="#ec0062")
                self.config(bg="#ec0062")
                trie.configure(state='disabled',cursor='arrow')
                print(P)
                return True
            elif len(P)==0 and Case.filledlist[self.id]==0:
                self.label.config(bg="#ec0062")
                self.option.config(bg="#ec0062")
                self.config(bg="#ec0062")
                return True
            else:
                if Case.filledlist[self.id]==0:
                    Case.filledlist[self.id]=1
                    Case.nbremptycase-=1
                self.label.config(bg="#28B463")
                self.option.config(bg="#28B463")
                self.config(bg="#28B463")
                if Case.nbremptycase==0:
                    trie.configure(state='active',cursor="hand2")
                print(P)    
                return True    
          
        else :
            #P=P[:-2]
            limitexceeded.config(text="Only number !")
            window.bell()
            print(P)
            return False
    """except ValueError:
        limitexceeded.configure(text="Only number")
        return False """

class Newcase(tk.Frame):
    def __init__(self, parent,j):
        tk.Frame.__init__(self, parent,borderwidth=1,width=1,height=25,bg="#3a8cff",cursor="hand2")
        self.grid(row=j//20,column=j % 20,padx=3,pady=12)
        self.id=j//2
        self.bind("<Enter>",self.displayaddbox)
        self.bind("<Leave>",self.hideaddbox)
        self.bind("<Button-1>", self.addbox)    

    def addbox(self,e,s=0):
        global cases
        global newcases
        values=[]
        n=nbrcase.get()
        newboxid=self.id+s
        Case.filledlist.insert(newboxid,0)
        Case.nbremptycase+=1
        for widget in result.winfo_children():
           widget.destroy()
        restxt.pack_forget()   
        trie.config(state=DISABLED)
        nbrcase.configure(state='normal')
        nbrcase.delete(0,END)
        nbrcase.insert(0,str(int(n)+1))
        nbrcase.config(state='disabled')
        cases=[]
        newcases=[]
        
        for box in data.winfo_children():
            if type(box)==Newcase:
                print(box.id)
                box.destroy()
        for box in data.winfo_children():
            values.append(box.entry.get())
            box.destroy()
        values.insert(newboxid,"")
        for i in range(len(values)*2):
            if i % 2 == 0:
                newcases.append(Newcase(data,i))
            else:    
                cases.append(Case(data,i))
                cases[i//2].entry.insert(0,values[i//2])
        cases[newboxid].entry.focus_set()
        newcases.append(Newcase(data,2*int(n)+2))

    def displayaddbox(self,e):
        buttondes.config(text="add new box")
        self.config(width=5,height=45,bg="#ec0062")
        self.pack_forget()
        self.grid(row=self.id*2//20,column=self.id*2 % 20,padx=1,pady=10)

    def hideaddbox(self,e):
        buttondes.config(text="Add left box (ctrl+l) / Add right box (ctrl+r)")
        self.config(width=1,height=25,bg="#3a8cff")
        self.pack_forget()
        self.grid(row=self.id*2//20,column=self.id*2 % 20,padx=3,pady=12)

window = tk.Tk()
    #variables 
window.geometry('900x600+222+40')
radioValue = tk.IntVar() 
typetrie=tk.StringVar()
value=tk.StringVar()
trietypes=["insertion","bulle"]
instractionfr=tk.Frame(master=window)
buttonfr=tk.Frame(master=window)
sortimage=PhotoImage(file='sort.png')
clearimage=PhotoImage(file='cancel.png')
createimage=PhotoImage(file='table.png')
deletenumberimage=PhotoImage(file='deletenumber.png')
deleteboximage=PhotoImage(file='deletebox.png')
datadesig=tk.Frame(master=window)
size=0

#scrollbar creation

parentfr=Frame(master=window)

workspace=tk.Canvas(master=parentfr,width=867,height=365)

scroll=ttk.Scrollbar(master=parentfr,orient=VERTICAL, command=workspace.yview)

workspace.configure(yscrollcommand=scroll.set)
boxesframe=tk.Frame(workspace)
workspace.bind("<Configure>",lambda e: workspace.configure(scrollregion=workspace.bbox('no')))
workspace.create_window((5,5),window=boxesframe,anchor="nw")
scroll.config(orient=VERTICAL,command=workspace.yview)


data=tk.Frame(master=boxesframe)
datadesig=tk.Frame(master=boxesframe)
resultdesig=tk.Frame(master=boxesframe)
result=tk.Frame(master=boxesframe)
restxt=tk.Label(master=resultdesig,text="The sorted list :",font = ('calibre',12,'bold'))
datatxt=tk.Label(master=resultdesig,text="Fill the boxes :",font = ('calibre',12,'bold'))
cases=[]
newcases=[]
valueslist=[]
frequency = 2000  # Set Frequency To 2500 Hertz
duration = 200  # Set Duration To 1000 ms == 1 second

#functions

"""def gettype():
    global nbrcase2
    nbrcase2=tk.Label(text=typetrie.get()+"  "+str(radioValue.get())).pack(padx=5,pady=5)

def hideerrmsg():
    errormsg.config(text="")"""
def validatenumcase(S,P):
    if S=='':
        return True
    try:
        if len(P)==1 and S=='0':
           int('a')
        int(S)
        errormsg.config(text="")
        return True
    except ValueError:
        """winsound.Beep(frequency, duration)"""
        window.bell()
        errormsg.config(text="Enter a positive number not null")
        return False

def clearlist():
    global valueslist
    global cases
    cases=[]
    #newcases=[]
    valueslist=[]
    nbrcase.config(state='normal')
    nbrcase.delete(0,END)
    restxt.pack_forget()
    datatxt.pack_forget()
    for widget in data.winfo_children():
          widget.destroy()
    for widget in result.winfo_children():
          widget.destroy()

    trie.configure(state='disabled',cursor="arrow")
    nbrcase.configure(state='normal')
    clear.configure(state='disabled')
    clear.configure(cursor='arrow')
    creat.configure(state='active',cursor="hand2")
    nbrcase.focus_set()

def creatlist(n):
    global cases
    global newcases
    global valueslist
    valueslist=[]
    try:
        n=int(n)
        if(int(n)<=0):
            errormsg.configure(text="Enter a positive number not null please")
        Case.nbremptycase=n
        Case.filledlist=[0]*n
        for widget in result.winfo_children():
            widget.destroy()
        datatxt.pack(padx=5,pady=5)
        for j in range(2*n):
            if j % 2 == 0:
                newcases.append(Newcase(data,j))
            else:    
                cases.append(Case(data,j))
        newcases.append(Newcase(data,2*n))        
        nbrcase.configure(state='disabled')
        creat.configure(state='disabled')
        creat.configure(cursor='arrow')
        clear.configure(state='active',cursor="hand2")
        cases[0].entry.focus_set()
        buttondes.config(text="Add left box (ctrl+l) / Add right box (ctrl+r)")
    except ValueError:
        errormsg.configure(text="Enter a positive number not null")

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
    restxt.pack(padx=5,pady=5)
    for case in cases:
      tried = tk.Frame(
            master=result,
            relief=tk.RAISED,
            borderwidth=1,
            bg="#ffc30f"
      )
      tried.grid(row=(i//10)+10,column=i % 10,padx=5,pady=5)
      index=tk.Label(master=tried,text=f"Index : {i+1}",bg="#ffc30f")
      value=tk.Entry(master=tried,justify=CENTER,width=10,font = ('calibre',10,'bold'))
      if radioValue.get()==0:
          value.insert(1,f"{valueslist[i]}")
      else:
          value.insert(1,f"{valueslist[-i-1]}")
      value.config(state="readonly")       
      i+=1
      index.pack()
      value.pack()



def enterkey():
    try:
        if creat['state']==tk.DISABLED:
            print(5/0)
        creatlist(nbrcase.get())
    except ZeroDivisionError:
        trielist()    

def clearkey():
   clearlist()

def deletekey():
   w=instractionfr.focus_get()
   f=w.master
   if f.master==data:
       f.delete()

def addrightkey():
    w=instractionfr.focus_get()
    f=w.master
    if f.master==data:
       newcases[f.id].addbox(e,s=1)

def addleftkey():
    w=instractionfr.focus_get()
    f=w.master
    if f.master==data:
       newcases[f.id].addbox(e)

def displaycreatdesg(e):
    buttondes.config(text="Create (Enter)") 

def displaycleardesg(e):
    buttondes.config(text="Clear (ctrl+c)")  

def displaytriedesg(e):
    buttondes.config(text="Sort (Enter)")       

def hidedesg(e):
    buttondes.config(text="Add left box (ctrl+l) / Add right box (ctrl+r)") 

#widgets created
typeoftrie=tk.Label(master=instractionfr,text="Choose the direction",font = ('calibre',12,'bold')) 
asc = tk.Radiobutton(master=instractionfr, text='ASC',variable=radioValue,value=0,
font = ('calibre',10,'bold'),cursor="hand2") 
desc = tk.Radiobutton(master=instractionfr, text='DESC',variable=radioValue, value=1,
font = ('calibre',10,'bold'),cursor="hand2")

typetext=tk.Label(master=instractionfr,text="Pick the type of sorting",font = ('calibre',12,'bold')) 
typelist = ttk.Combobox(master=instractionfr, values = trietypes,textvariable=typetrie,
                         font = ('calibre',10,'bold'),cursor="hand2")
typelist.set("insertion")

vncmd = (tk.Label(master=instractionfr,text="Enter the length").register(validatenumcase),'%P','%S')
nbrtext=tk.Label(master=instractionfr,text="Enter the length",font = ('calibre',12,'bold'))
nbrcase=tk.Entry(master=instractionfr,justify=CENTER,validate="key",
                  validatecommand=vncmd,font = ('calibre',12,'bold'))
nbrcase.focus_set()      
creat=tk.Button(master=buttonfr,image=createimage,command= lambda :creatlist(nbrcase.get()),
                font = ('calibre',12,'bold') ,width=40,height=40,cursor="hand2")
clear=tk.Button(master=buttonfr,image=clearimage,command= lambda :clearlist(),state=DISABLED,
               font = ('calibre',12,'bold'),width=40,height=40,cursor="arrow")
trie=tk.Button(master=buttonfr,image=sortimage,command= lambda :trielist(),
state=DISABLED,font = ('calibre',12,'bold'),width=40,height=40,cursor="arrow")
errormsg=tk.Label(master=instractionfr,text="",fg="red",font = ('calibre',12,'bold'))
limitexceeded=tk.Label(master=window,text="",font = ('calibre',12,'bold'),fg="red")
datatxt=tk.Label(master=datadesig,text="Fill the boxes:",font = ('calibre',12,'bold'))
buttondes=tk.Label(window,text="",bd=1,relief=SUNKEN,anchor=E)

#tip.bind_widget(clear,balloonmsg="Creat (ctrl+c)")
"""#Create a tooltip
tip= Balloon(window)

#Create a Button widget
my_button=Button(window, text= "Python", font=('Helvetica bold', 20))
my_button.pack(pady=20)

#Bind the tooltip with button
tip.bind_widget(my_button,balloonmsg="Python programming language")"""



#emplacement of Widgets
instractionfr.pack(padx=5,pady=5)
typeoftrie.grid(column=0,row=0,padx=50)
asc.grid(column=0,row=1,padx=50)
desc.grid(column=0,row=2,padx=50)
typetext.grid(column=2,row=0,padx=50)
typelist.grid(column=2,row=1,padx=50)
nbrtext.grid(column=1,row=0,padx=50)
nbrcase.grid(column=1,row=1,padx=50)
errormsg.grid(column=1,row=2)

buttonfr.pack(padx=5,pady=5)
creat.grid(column=0,row=0,padx=5)
clear.grid(column=2,row=0,padx=5)
trie.grid(column=1,row=0,padx=5)
limitexceeded.pack(padx=5,pady=5)
buttondes.pack(fill=X,side=BOTTOM,ipady=2)


parentfr.pack()
workspace.pack(side=LEFT,fill=BOTH,expand=1)
scroll.pack(side=RIGHT,fill=Y)
datadesig.pack()
data.pack()
resultdesig.pack()
result.pack()
window.title("HT. Salmen Sorting Program")
window.resizable(False,False)

#mouse
creat.bind("<Enter>",displaycreatdesg)
trie.bind("<Enter>",displaytriedesg)
clear.bind("<Enter>",displaycleardesg)
creat.bind("<Leave>",hidedesg)
trie.bind("<Leave>",hidedesg)
clear.bind("<Leave>",hidedesg)

#keyboard
window.bind('<Return>',lambda event: enterkey())
window.bind_all('<Control-Key-c>',lambda event: clearkey())
window.bind_all('<Control-Key-d>',lambda event: deletekey())
window.bind_all('<Control-Key-r>',lambda event: addrightkey())
window.bind_all('<Control-Key-l>',lambda event: addleftkey())
#window.bind('<key>',lambda event: test())
window.mainloop()