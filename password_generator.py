import string
import tkinter
from tkinter import *
from tkinter import messagebox
import time
def randominlist(list1):
 n=1
 l=len(list1)
 while(n==1):
  time.sleep(.00001)
  nano_sec = int(time.time() * 1000000000000000)
  a = nano_sec%100
  if(a>=0 and a<l):
         return list1[a]
         n=0

def ranrange(b,c):
 n=1
 while(n==1):
  nano_sec = int(time.time() * 1000000000000000)
  a = nano_sec%100
  if(a>=b and a<=c):
         return a
         n=0
topp = tkinter.Tk()
topp.minsize(500, 250)
def password():
  letters = string.ascii_letters+string.digits+'@#$%&!'
  uppercasel=string.ascii_uppercase
  lowercasel=string.ascii_lowercase
  dig=string.digits
  length=ranrange(12,32)
  time.sleep(.00001)
  pas=''.join(randominlist(letters) for n in range(length))
  time.sleep(.00001)
  list1=list(pas)
  list1[0]=randominlist(lowercasel)
  time.sleep(.00001)
  list1[length-1]=randominlist(uppercasel)
  time.sleep(.00001)
  a=ranrange(1,length-2)
  list1[a]=randominlist(uppercasel)
  time.sleep(.00001)
  b=randominlist([i for i in range(1,length-1) if i not in [a]])
  list1[b]=randominlist(lowercasel)
  time.sleep(.00001)
  c=randominlist([i for i in range(1,length-1) if i not in [a,b]])
  time.sleep(.00001)
  list1[c]=randominlist('@#$%&!')
  time.sleep(.00001)
  d=randominlist([i for i in range(1,length-1) if i not in [a,b,c]])
  time.sleep(.00001)
  list1[d]=randominlist(dig)
  time.sleep(.00001)
  passs = ""
  for i in list1:
    passs += i
  messagebox.showinfo("Password","Random Password is   "+passs)
topp.configure(bg="white")
Label(topp, bg="white",text = 'Random Password Generator',  font =('Arial', 15)).pack(side = TOP, pady = 10)
Label(topp, bg="white",text = 'Created By- Esha  Rollno 2014653',  font =('Arial', 10)).pack(side = BOTTOM , pady = 10,anchor=S)
B = tkinter.Button(topp, text ="**Generate Random Password**", command = password)
B.configure(bg = "Black",fg="white")
B.pack()
topp.mainloop()
