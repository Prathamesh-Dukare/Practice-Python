from tkinter import *
root=Tk()
root.title('Srollbar')
root.geometry("400x300")

scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill='y')
listbox=Listbox(root,yscrollcommand=scrollbar.set)

for i in range(20):
    listbox.insert(END,f'Item {i}')
    listbox.pack()

scrollbar.config(command=listbox.yview)











root.mainloop()