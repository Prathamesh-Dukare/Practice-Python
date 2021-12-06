from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x300')
        self.title("GUI Using OOPs")

    def stutusbar(self):
        var=StringVar()
        var.set('Ready')
        slabel=Label(textvar=var,relief=SUNKEN,anchor='w')
        slabel.pack(side=BOTTOM,fill=X)
    
    def click(self):
        print('Button Clicked')

    def creatbutton(self,btext):
        Button(text=btext,command=self.click).pack()



window=GUI()

window.creatbutton('Button1')
window.stutusbar()
window.mainloop()










               