from tkinter import *


def cambio_colore():
    testo.configure(text=casella_testo.get())
    f.configure(background="cyan")
    testo.configure(background="cyan")


    
f = Tk()

f.title("Finestra")
f.geometry("300x300")
f.configure(background="yellow")

testo = Label(f, text="Salve!", font="Arial 14 bold", background="yellow")
testo.pack()


casella_testo = Entry(f)
casella_testo.pack(pady=15)
casella_testo.focus_set()#mette il cursore in partenza su Entry



b = Button(f, text="premi qui", font="Arial 14 bold", command=cambio_colore)
b.configure(cursor="hand2")
b.pack()



f.mainloop()
