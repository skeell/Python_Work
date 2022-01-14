from tkinter import *
#from tkinter import messagebox

def test():
    pass


f = Tk()

testo = Text(f, bg="yellow", font="Arial", insertbackground="pink",
             insertwidth=10)#insertwidth spessore cursore
testo.focus()
testo.pack()


b = Button(f, text="PREMI", command=test)
b.pack()


f.mainloop()
 

