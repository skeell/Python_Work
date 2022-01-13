from tkinter import *


def cambio_colore(evento): #evento attiva il bind
    testo.configure(text=casella_testo.get())
    f.configure(background="cyan")
    testo.configure(background="cyan")


def elimina():
    casella_testo.delete(0, END)


    
f = Tk()

f.title("Finestra")
f.geometry("300x300")
f.configure(background="yellow")

testo = Label(f, text="Salve!", font="Arial 14 bold", background="yellow")
testo.pack()


casella_testo = Entry(f, show="*")# il parametro "show" converte i caratteri inseriti 
casella_testo.pack(pady=15)
casella_testo.focus_set()#mette il cursore in partenza su Entry
casella_testo.configure(justify=CENTER) # mette il cursore al centro
casella_testo.bind("<Return>", cambio_colore)

b = Button(f, text="premi qui", font="Arial 14 bold", command=cambio_colore)
b.configure(cursor="hand2")
b.pack()

b1 = Button(f, text="cancella", font="Arial 14 bold", command=elimina)
b1.configure(cursor="hand2")
b1.pack()


f.mainloop()
