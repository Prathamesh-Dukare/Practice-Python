from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
root=Tk()
root.geometry("500x350")
root.title("Untitled-Notepad")
#root.wm_iconbitmap('a.png')

def newfile():
    global file
    root.title('Untitled-Notepad')
    file=None
    textarea.delete(1.0,END)

def openfile():
    global file
    file=askopenfilename(defaultextension='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])
    if(file==''):
        file=None
    else:
        root.title(os.path.basename(file)+'-Notepad')
        textarea.delete(1.0,END)
        f=open(file,'r')
        textarea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if(file==None):
        file=asksaveasfilename()()(initialfile='Untitled.txt',defaultextensions='.txt',filetypes=[('All Files','*.*'),('Text Documents','*.txt')])

        if(file==''):
            file=None
        else:
            #save as new file
            f=open(file,'w')
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+'Untitled-Notepad')
    else:
        #savethefile
        f=open(file,'w')
        f.write(textarea.get(1.0,END))
        f.close()

def exitfile():
    root.destroy()

def undo():
    pass
def cut():
    textarea.event_generate(('<<Cut>>'))
def copy():
    textarea.event_generate(('<<Copy>>'))
def paste():
    textarea.event_generate(('<<Paste>>'))

def feedback():
    pass
def about():
    showinfo("Notepad",'Made by Duke')





mymenu=Menu(root)
m1=Menu(mymenu,tearoff=0)
m1.add_command(label='New',command=newfile)
m1.add_command(label='Open',command=openfile)
m1.add_command(label='Save',command=savefile)
#m1.add_command(label='Save as',command=openfile)
m1.add_command(label='Exit',command=exitfile)
mymenu.add_cascade(label="File",menu=m1)

m2=Menu(mymenu,tearoff=0)
m2.add_command(label='Undo',command=undo)
m2.add_command(label='Cut',command=cut)
m2.add_command(label='Copy',command=copy)
m2.add_command(label='Paste',command=paste)
mymenu.add_cascade(label="Edit",menu=m2)

m3=Menu(mymenu,tearoff=0)
m3.add_command(label='Send Feedback',command=feedback)
m3.add_command(label='About Notepad',command=about)
mymenu.add_cascade(label="Help",menu=m3)

textarea=Text(root,font='lucida 15')
textarea.pack(fill=BOTH,expand=True)
file=None

scroll=Scrollbar(textarea)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=textarea.yview)
textarea.config(yscrollcommand=scroll.set)

root.config(menu=mymenu)

root.mainloop()
