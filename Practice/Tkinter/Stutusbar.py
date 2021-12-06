from tkinter import *
root=Tk()
root.geometry('500x200')
root.title('Stutusbar')



def upload():
    import time
   
    statusvar.set('Stutus : Uploading File...')
    slabel.update()
    time.sleep(4)
    statusvar.set('Stutus : Ready')

    


statusvar=StringVar()
statusvar.set('Stutus : Ready')


slabel=Label(root,textvariable=statusvar,relief=SUNKEN,anchor='w')
slabel.pack(side=BOTTOM,fill=X)


button=Button(root,text='Upload File',command=upload)
button.pack()













root.mainloop()