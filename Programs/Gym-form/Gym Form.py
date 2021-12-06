from tkinter import *
#GYM REGISTRATION FORM
root=Tk()
root.geometry("550x300")
root.title("GYM REGISTRATION FORM")
Label(text='GYM REGISTRATION FORM',padx=50,pady=15,font='Arial 15 bold').grid(row=0,column=0)

def sub():
    print('Form Submtted Succesfully!')
    with open('records.txt','a') as f:
        f.write(f'name : {Namevar.get()}\n Addres : {Addresvar.get()}\n Age : {Agevar.get()}\n Gender :{Gendervar.get()}\n Phone : {Phonevar.get()}\n Payments :{Paymentsvar.get()}\n\n')

Label(root,text='Name').grid()
Label(root,text='Addres').grid()
Label(root,text='Age').grid()
Label(root,text='Gender').grid()
Label(root,text='Phone').grid()
Label(root,text='Payments').grid()

Namevar=StringVar()
Addresvar=StringVar()
Agevar=StringVar()
Gendervar=StringVar()
Phonevar=StringVar()
Paymentsvar=StringVar()
tandcvar=IntVar()

Entry(root,textvariable=Namevar).grid(row=1,column=1)
Entry(root,textvariable=Addresvar).grid(row=2,column=1)
Entry(root,textvariable=Agevar).grid(row=3,column=1)
Entry(root,textvariable=Gendervar).grid(row=4,column=1)
Entry(root,textvariable=Phonevar).grid(row=5,column=1)
Entry(root,textvariable=Paymentsvar).grid(row=6,column=1)


Checkbutton(text='Agree to terms & conditions',variable=tandcvar,padx=100,pady=5).grid()
Button(text="SUBMIT FORM",command=sub).grid()
root.mainloop()