from tkinter import *

def esegui():
    print(metro.get())


f = Tk()


f.title("Finestra")
f.geometry("400x400")
f.configure(background="yellow")

metro = Scale(f, from_=0, to_=10, orient=HORIZONTAL)
metro.set(3)#setta la scala a valore predefinito
metro.pack()

b = Button(f, text="premi qui", command=esegui)
b.pack()

f.mainloop()
 
