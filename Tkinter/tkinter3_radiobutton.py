from tkinter import *

def esegui():
    print(valore.get())


f = Tk()

valore = StringVar()

f.title("Finestra")
f.geometry("400x400")
f.configure(background="yellow")

scelta = Radiobutton(f, text="Maschio", variable=valore, value="Maschio")
scelta.pack()

scelta2 = Radiobutton(f, text="Femmina",variable=valore, value="Femmina")
scelta2.pack()


b = Button(f, text="Click_Me", command=esegui)
b.pack()
f.mainloop()
 
