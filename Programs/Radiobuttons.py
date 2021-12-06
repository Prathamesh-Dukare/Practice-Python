from tkinter import *
import tkinter.messagebox as tmsg

root=Tk()
root.geometry("400x170")
root.title('Radiobutton')

def order():
    tmsg.showinfo('Order Stutus',f'Order Succesful for {var.get()}')

var=StringVar()
var.set('radio')
#var=IntVar()
Label(root,text='What Would You Take?',font='Arial 15 bold').pack()
radio=Radiobutton(root,text='Dosa',variable=var,value='Dosa').pack()
radio=Radiobutton(root,text='Samosa',variable=var,value='Samosa').pack()
radio=Radiobutton(root,text='Pakode',variable=var,value='Pakode').pack()
radio=Radiobutton(root,text='Idly',variable=var,value='Idly').pack()

Button(root,text='Order Now',command=order).pack()

root.mainloop()