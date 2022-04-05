from tkinter import *

root=Tk()

miFrame=Frame(root)
miFrame.pack()

miImagen=PhotoImage(file='asikaemo.gif')

miLabel=Label(miFrame,image=miImagen,width='800',height='800')
miLabel.config()
miLabel.pack()



root.mainloop()
