from tkinter import *


def cambio_colore():
    f.configure(background="cyan")
    testo.configure(background="cyan")


    
f = Tk()

f.title("Finestra")
f.geometry("300x300")
f.configure(background="yellow")

testo = Label(f, text="Hello World!",background="yellow", fg="red" )
testo.pack(side=TOP, pady=15)

#testo1 = Label(f, text="Hello\nsud World!",background="yellow", fg="red",
               #font="Arial 22 bold")
#testo1.pack(side=TOP)
#testo1.configure(cursor="hand2")

b = Button(f, text="premi qui", font="Arial 14 bold", command=cambio_colore)
b.configure(cursor="hand2")
b.pack()



f.mainloop()
