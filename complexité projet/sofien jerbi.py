import tkinter as tk
####################################################################
def isfloat(num):# function to check if num is a float
    try:
        float(num)
        return True
    except ValueError:
        return False
####################################################################

def mergeSort(arr):# mergesort sorting algorithm
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
  
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
######################################################################
def callback(input):
    try:  
        if isfloat(input) or (input[0] == "-" and (input[1:] == "" or isfloat(input[1:]))):
            return True 
        else:
            return False
    except IndexError:
        if isfloat(input) or input=="-" or input =="":
            return True
        else:
            return False 
######################################################################
def fill():# function that handles filling the array L with values from all the Entries
    global L
    global flag
    L=[float(i.get()) for i in entry if isfloat(i.get())]# puts every input that's a float into L --- L should be empty firsthand which happens in Sort
    
    if (not len(L)==len(entry)):#checks if L is the same size as the number of input fields
                                #should only fail if one or more of those fields is NaN

        lbl_array_input["text"]="Make sure you fill all the fields correctly"#actions to take if the check fails
        lbl_array_input["fg"]="red"
        flag = False #set flag to false

    else:
        lbl_array_input["text"]="Please enter your array elements"#reset the label after the user fixes the input
        lbl_array_input["fg"]="black"
        flag = True #set flag to true

#######################################################################    

def Sort(event):
    global L
    global sortedarray
    global ent_input
    for i in frm_sorted_array.winfo_children():
        i.destroy()
    lbl_sorted_array = tk.Label(master=frm_sorted_array,text="The array after it has been sorted is:")
    L=[]
    fill()
    if flag:
        mergeSort(L)
        lbl_sorted_array.grid(row=0,column=0,columnspan=n)
        for x,i in enumerate(L):
            lbl_out = tk.Label(master=frm_sorted_array,text=f"{i}",width=4)
            sortedarray.append(lbl_out)
            lbl_out.grid(row=(x//10)+1,column=x%10,padx=4)
        ent_input.focus_set()
            
########################################################################

def size_update(event):
    print(event.char)
    global n 
    global entry
    global reg
    n = ent_input.get()
    n=int(n)
    for x,i in reversed(list(enumerate(entry))):
        i.destroy()
        entry.pop(x)
    
    lbl_input["fg"]="black"
    lbl_input["text"]="Please enter your array size"
    for i in range(n):
        ent_array = tk.Entry(master=frm_unsorted_array,width=4)
        ent_array.config(validate="key",validatecommand =(reg, '%P'))
        ent_array.bind("<Return>",Sort)
        entry.append(ent_array)
        ent_array.grid(row=(i//10)+1,column=i%10,padx=5,pady=3)
    lastrow,_=frm_unsorted_array.grid_size()
    btn_sort.grid(row=lastrow,columnspan=min(n,10))
    lbl_array_input.grid(row=0,column=0,columnspan=n)
    entry[0].focus_set()

###########################################################################
        
if __name__ == '__main__':
    entry=[]
    L=[]
    sortedarray=[]
    n=1
    flag = True

    window = tk.Tk() #main window

    window.title("Sorting project")
    windowWidth = 450
    windowHeight = 500
    print("Width",windowWidth,"Height",windowHeight)
    positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(window.winfo_screenheight()/2.1 - windowHeight/2)

    window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
    window.minsize(400,400)
    window.resizable(False,False)

    reg = window.register(callback)

    frm_input=tk.Frame(
        master = window,
        borderwidth=1
    )#frame for handling array size input
    
    frm_unsorted_array=tk.Frame(
        master=window,
        borderwidth=1
    )#frame for handling array value inputs

    frm_sorted_array=tk.Frame(
        master=window,
        borderwidth=1
    )#frame for displaying the sorted array

    window.columnconfigure(0,weight=1)
    window.rowconfigure([0,1,2],weight=1)

    lbl_input = tk.Label(master=frm_input,text="Please enter your array size")
    ent_input = tk.Entry(master=frm_input)
    ent_input.focus_set()
    ent_input.bind("<Return>",size_update)
    ent_input.config(validate="key",validatecommand =(reg, '%P'))
    btn_input = tk.Button(master=frm_input,text="Submit",anchor=tk.CENTER)
    btn_input.bind("<Button-1>",size_update)

    lbl_array_input = tk.Label(master=frm_unsorted_array,text="Please enter your array elements")
    btn_sort = tk.Button(master = frm_unsorted_array,text="Sort")
    btn_sort.bind("<Button-1>",Sort)

    

    lbl_input.pack()
    ent_input.pack()
    btn_input.pack()

    frm_input.pack(pady=5)
    frm_unsorted_array.pack(pady=5)
    frm_sorted_array.pack(pady=5)
    
    

    window.mainloop()