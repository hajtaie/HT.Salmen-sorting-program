from operator import le
import random 

def bulle(l):
    n=len(l)
    while 1:
        permutation=False
        for i in range(1,n):
            if l[i]<l[i-1]:
                l[i],l[i-1]=l[i-1],l[i]
                permutation = True
        if not permutation:
            break
        n=n-1 


def insertion(l):
    for i in range(len(l)):
        x=l[i]
        j=i
        #décalage des éléments de la liste
        while j>0 and l[j-1]>x:
            l[j]=l[j-1]
            j=j-1
        #on insére l'élément à sa place
        l[j]=x    

def posmin(l):
    p=0
    for i in range(1,len(l)):
        if l[i]<l[p]:
            p=i
    return p

def selection(l):
    for i in range(len(l)):
        p=posmin(l[i:])
        l[i],l[p+i]=l[p+i],l[i]


"""def partquicksort(l):
    start=0
    end=len(l)-1
    pivot=8
    while start<end:
        while l[start]<l[pivot]:
            start+=1
        while l[end]>l[end]:
            end-=1
        l[start],l[end]=l[end],l[start]        
        
          
           
l=[5,86,69,73,11,17,1,74,34,3]
partquicksort(l)
print(l)"""