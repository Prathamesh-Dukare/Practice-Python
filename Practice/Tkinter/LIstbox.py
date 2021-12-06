from tkinter import *
root=Tk()
root.geometry('400x300')
root.title('Listbox')

def add():
    lbx.insert(ACTIVE,f'Another Item')
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,'First Item')


Button(root,text='Add Item',command=add).pack()













root.mainloop()