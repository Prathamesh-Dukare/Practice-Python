from tkinter import *

root=Tk()
root.title('Resizer')
root.geometry('200x150')

def apply():
    root.geometry(f'{widthvar.get()}x{heightvar.get()}')
Label(root,text='Enter Width').grid()
Label(root,text="Enter Height").grid()

widthvar=StringVar()
heightvar=StringVar()
Entry(root,textvariable=widthvar).grid(row=0,column=1)
Entry(root,textvariable=heightvar).grid(row=1,column=1)

Button(root,text='Apply',command=apply).grid()



root.mainloop()


