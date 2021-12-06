from tkinter import *

root=Tk()
root.geometry("500x350")
root.title("My First GUI")
var=Label(text="Hello World !",background="red",padx=700,pady=0,font='Arial 16 italic',relief=SUNKEN)
var.pack()

f1=Frame(root,bg="grey",borderwidth=5,relief=SUNKEN,padx=0,pady=0)
f1.pack(side=LEFT,fill='y')
l1=Label(f1,text="Explorer",font='Arial 18 italic',padx=120)
l1.pack(side=TOP)

f2=Frame(root,bg="grey",borderwidth=5,relief=SUNKEN)
f2.pack(side=TOP,padx=0,pady=0,fill='x')
l2=Label(f2,text="Opened files",font='monospace 18 italic',pady=0)
l2.pack()

def name():
    print('File 1 open')
def name1():
    print('File 2 open')
def name2():
    print('File 3 open')



b1=Button(f1,text='Main Files',background="green",padx=120,pady=5, relief=RAISED,font='monospace 12 bold')
b1.pack()
b2=Button(f1,text='File1',background="green",padx=60,pady=5, relief=RAISED,font='monospace 12 italic',command=name)
b2.pack()
b3=Button(f1,text='File2',background="green",padx=60,pady=5, relief=RAISED,font='monospace 12 italic',command=name1)
b3.pack()
b4=Button(f1,text='File3',background="green",padx=60,pady=5, relief=RAISED,font='monospace 12 italic',command=name2)
b4.pack()


root.mainloop()
