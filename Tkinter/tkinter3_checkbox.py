from tkinter import *


def controlla():
    print(valore.get())

    
f = Tk()

#valore = IntVar()
valore = StringVar()

f.title("Finestra")
f.geometry("400x400")
f.configure(background="yellow")

#casella = Checkbutton(f, bg="yellow", text="Seleziona_Qui",
                      #variable=valore, command=controlla)
casella = Checkbutton(f, bg="yellow", text="conosci la risposta?",
                      onvalue="si", offvalue="no", variable=valore, command=controlla)
casella.pack(pady=5)
casella.select() #casella spuntata all'avvio
#casella.deselect() # non spuntata

f.mainloop()
 
