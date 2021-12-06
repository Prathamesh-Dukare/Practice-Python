from tkinter import *

root=Tk()
root.geometry("500x350")
root.title("My First GUI")
var=Label(text="Hello World !",background="green",padx=12,pady=1,font='Arial 16 italic')
var.pack()

img=PhotoImage(file="a.png")
imglabel=Label(image=img)
imglabel.pack()

root.mainloop()






