from tkinter import *


def scrivi(evento):
    x = lista.curselection()[0]
    print(lista.get(x))
    
f = Tk()


f.title("Finestra")
f.geometry("400x400")
f.configure(background="yellow")


lista = Listbox(f)
lista.pack()
lista.insert(END, "uno", "due", "tre", "quattro")
lista.insert(0, "QUI COMINCIA")
lista.delete(3,4)#cancella dati in listbox
lista.bind("<ButtonRelease-1>", scrivi)#comanda tasto dx del mouse

f.mainloop()
 
