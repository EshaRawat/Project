import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
def encrypt(imagebyte,key): #function to encrypt reciveing image in form of array of bytes and key
    for i in range(len(imagebyte)):
        #overriting array of bytes by doing xor with array element and key
        imagebyte[i]=imagebyte[i]^key
    return imagebyte

def decrypt(imagebyte,key): #function to decrypt reciveing image in form of array of bytes and key
    for i in range(len(imagebyte)):
        #overriting array of bytes by doing xor with array element and key
        imagebyte[i]=imagebyte[i]^key
    return imagebyte
def openfile():
    #opemimg image files from explorer
    file = filedialog.askopenfilename(filetypes=[('Image Files', '*.jpg'),('Image Files', '*.jpeg'),('Image Files', '*.png')])
    path.set(file)#returning path of selected file
def start(path,key,choice,check,check1,check2):
    try:
        #converting stringvar to string and itn var to int by get()
        path=path.get()
        key1=int(key.get())
        check=check.get()
        check1=check1.get()
        check2=check2.get()
        with open(path, "rb") as image:
            ir = image.read() #reading image from directory
            imagebyte=bytearray(ir) #converting image to array of bytes
        if(choice==1):
            imagebyte=encrypt(imagebyte,key1) #calling encrypt function if choice is encrypt
            if(check==1):
                phrase="encryptedWithKey"+str(key1)+".jpg" #filename if key is not hidden
            else:
                phrase="encrypted.jpg"  #filename if key is hidden
            with open(path+phrase,'wb') as image:
                image.write(imagebyte) #storing image
            messagebox.showinfo(title='Done', message="Encryption done by key - "+str(key1)) #sohowinfo window
        if(choice==2):
            imagebyte=decrypt(imagebyte,key1) #calling decrypt function if choice is decrypt
            if(check1==0):
                with open(path+"decrypted.jpg",'wb') as image:
                    #storing image if no overwrite demanded
                    image.write(imagebyte)
            else:
                with open(path,'wb') as image:
                    #storing image by overriting
                    image.write(imagebyte)
            messagebox.showinfo(title='Done', message="Decryption done by key"+str(key1))  #sohowinfo window
        if(check2==1):
            #erasing key from input box
            key.set('')
    except Exception:
        #if any runtime error occured showerror window pops up
        messagebox.showerror(title='Error', message='Wrong Input')
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
root = tk.Tk()
root.title("Image Encrypt")#window name
root.configure(background="white")
root.geometry('307x207')
root.iconbitmap(resource_path("icon.ico"))#icon imported
root.resizable(True, True)
path=tk.StringVar()
key=tk.StringVar()
check=tk.IntVar()
check1=tk.IntVar()
check2=tk.IntVar()
#filepath label
pathlabel = tk.Label(root, text = 'File Path', font=('Helvetica',12, 'bold'),background="white",fg='#330000')
#path input
pathInput= tk.Entry(root,textvariable = path, font=('Helvetica',10,'normal'),background="white",fg='#330000')
#key label
keylabel = tk.Label(root, text = 'Password', font = ('Helvetica',12,'bold'),background="white",fg='#330000')
#key input with hidden characters
keyInput=tk.Entry(root, textvariable =key, font = ('Helvetica',10,'normal'), show = 'X',background="white",fg='#330000')
#encrypt and decrypt button calling start button via lambda
Encryptbtn=tk.Button(root,text = 'Encrypt',font = ('Times',12,'bold'), command=lambda: start(path,key,1,check,check1,check2),activebackground='red',background="white",fg='#003333')
Decryptbtn=tk.Button(root,text = 'Decrypt',font = ('Times',12,'bold'), command=lambda: start(path,key,2,check,check1,check2),activebackground='blue',background="white",fg='#003300')
#check buttons
C1 = tk.Checkbutton(root, text = "AttachKey", variable = check, onvalue = 1, offvalue = 0, height=1,font=('Helvetica',8) ,background="white",fg='#660000')
C2 = tk.Checkbutton(root, text = "Overwrite", variable = check1, onvalue = 1, offvalue = 0, height=1,font=('Helvetica',8) ,background="white",fg='#660000')
C3 = tk.Checkbutton(root, text = "EraseKey", variable = check2, onvalue = 1, offvalue = 0, height=1,font=('Helvetica',8) ,background="white",fg='#FF0000')
#browse button for opening explorer
B=tk.Button(root, text="Browse", command=openfile ,bg='white')
t1=tk.Label(root,text='Esha Rawat',bg='white',fg='#000033',font=('Helvetica',8,'normal'))
t2=tk.Label(root,text='2014653 ',bg='white',fg='#000033',font=('Helvetica',7,'normal'))
#arranging all elements in rows and columns
pathlabel.grid(row=0,column=0)
pathInput.grid(row=0,column=1)
B.grid(row=0,column=2)
keylabel.grid(row=1,column=0)
keyInput.grid(row=1,column=1)
Encryptbtn.grid(row=2,column=0)
Decryptbtn.grid(row=2,column=2)
C1.grid(row=3,column=0)
C2.grid(row=3,column=2)
C3.grid(row=1,column=2)
t1.grid(row=7)
t2.grid(row=8)
root.mainloop()#tkinterwindow loop
