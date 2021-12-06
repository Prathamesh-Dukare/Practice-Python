from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry('944x600')
root.title('Visual Studio Code')

def fun():
    val=tmsg.askquestion('Are You Sure')
    print(val)
    if(val=='yes'):
        msg="Executed"
    else:
        msg="Not Executed"
    tmsg.showinfo('Operation',msg)
def new():
    val=tmsg.askretrycancel('Windows System','File Creation Failed!')
    if(val):
        new()


mymenu=Menu(root)
m1=Menu(mymenu,tearoff=0)
m1.add_command(label='New File',command=new)
m1.add_command(label='Open File',command=fun)
mymenu.add_cascade(label='File',menu=m1)

m2=Menu(mymenu,tearoff=0)
m2.add_command(label='Undo',command=fun)
m2.add_command(label='Rndo',command=fun)
m2.add_command(label='Cut',command=fun)
m2.add_separator()
m2.add_command(label='Copy',command=fun)
m2.add_command(label='Paste',command=fun)
mymenu.add_cascade(label="Edit",menu=m2)

'''m3=Menu(mymenu,tearoff=0)
m3.add_command(label='Rate us here',command=)
mymenu.add_cascade(label='Rate Us',menu=m1)'''



root.config(menu=mymenu)
root.mainloop()
