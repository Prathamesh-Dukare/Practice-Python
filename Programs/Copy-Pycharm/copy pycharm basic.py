from tkinter import *

root=Tk()
root.geometry("500x350")
root.title("My First GUI")
var=Label(text="Hello World !",background="green",padx=700,pady=0,font='Arial 16 italic',relief=SUNKEN)
var.pack()

f1=Frame(root,bg="grey",borderwidth=5,relief=SUNKEN,padx=46,pady=20)
f1.pack(side=LEFT,fill='y')
l1=Label(f1,text="Explorer",font='Arial 18 italic')
l1.pack()

f2=Frame(root,bg="grey",borderwidth=5,relief=SUNKEN)
f2.pack(side=TOP,padx=0,pady=0,fill='x')
l2=Label(f2,text="Opened files",font='Arial 18 italic',pady=0)
l2.pack()
root.mainloop()
