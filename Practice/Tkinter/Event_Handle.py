from tkinter import *
root=Tk()
root.title('Events')
root.geometry('300x200')

def fun(event):
    print("CLicked")

    
button=Button(root,text='Close',padx=10,pady=5)
button.pack()

button.bind('<Button-1>',fun)












root.mainloop()