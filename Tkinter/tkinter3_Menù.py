from tkinter import *

def test(scelta):
    print("ciao")


f = Tk()


f.title("Finestra")
f.geometry("400x400")
f.configure(background="yellow")

trasparente = Menu(f)
f.config(menu=trasparente)
primo_menu = Menu(trasparente)
trasparente.add_cascade(label="File", menu=primo_menu)
primo_menu.add_command(label="Apri...", command=test, accelerator="Alt-a")
primo_menu.add_separator()
primo_menu.add_command(label="Esci", command=quit)

impostazioni = Menu(trasparente)
trasparente.add_cascade(label="Impostazioni", menu=impostazioni)
impostazioni.add_command(label="Cambio Colore Schermo", command=test)
impostazioni.add_command(label="Cambia Colore Testo", command=test)
impostazioni.add_command(label="Imposta Variabili", command=test)

f.bind("<Alt-a>", test) #presuppone presenza opzione in def

f.mainloop()
 

