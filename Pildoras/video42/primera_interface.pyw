from tkinter import *

raiz=Tk()

raiz.title('darkesthj.exe')

# raiz.resizable(False,False)

raiz.iconbitmap('eeee.ico')

raiz.geometry('800x500')

raiz.config(bg='black')

miFrame=Frame()

miFrame.pack(fill='y')

miFrame.config(bg='red')

miFrame.config(width='100',height='200')

miFrame.config(bd=25)

miFrame.config(relief='sunken')

miFrame.config(cursor='pirate')

raiz.mainloop()
