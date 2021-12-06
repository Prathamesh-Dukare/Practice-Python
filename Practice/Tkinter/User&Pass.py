from tkinter import *

root=Tk()
root.geometry("500x350")
root.title("My First GUI")

Label(root,text='Name').grid()
Label(root,text='Password').grid()

def sub():
    print(userval.get(),'submitted')
    
userval=StringVar()
passval=StringVar()
Entry(root,textvariable=userval).grid(row=0,column=1)
Entry(root,textvariable=passval).grid(row=1,column=1)
Button(text="Submit",command=sub).grid()

root.mainloop()