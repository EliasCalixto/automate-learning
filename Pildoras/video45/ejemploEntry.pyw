from tkinter import *

root=Tk()

myFrame=Frame(root,width=1200,height=600)
myFrame.pack()

cuadroTexto=Entry(myFrame)
cuadroTexto.grid(row=0,column=1)

nombreLabel=Label(myFrame,text='Nombre:')
nombreLabel.grid(row=0,column=0)



root.mainloop()
